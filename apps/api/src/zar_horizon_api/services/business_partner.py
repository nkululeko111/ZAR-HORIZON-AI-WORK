import csv
import hashlib
import io
import re
from collections import defaultdict
from dataclasses import dataclass, replace
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Iterable, Protocol


CENT = Decimal("0.01")
MAX_CSV_ROWS = 10_000
MAX_CSV_BYTES = 2_000_000


class CSVFormatError(ValueError):
    pass


class TransactionLike(Protocol):
    transaction_date: date
    description: str
    transaction_type: str
    category: str
    amount: Decimal
    currency: str


@dataclass(frozen=True)
class ParsedTransaction:
    line_number: int
    status: str
    errors: tuple[str, ...]
    transaction_date: date | None
    description: str | None
    transaction_type: str | None
    category: str | None
    amount: Decimal | None
    currency: str | None
    source_reference: str | None
    fingerprint: str | None


def _header_name(value: str) -> str:
    return re.sub(r"[\s_-]+", " ", value.strip().lstrip("\ufeff").lower())


HEADER_ALIASES = {
    "date": {"date", "transaction date"},
    "description": {"description", "details", "memo", "narrative"},
    "amount": {"amount", "value"},
    "currency": {"currency", "currency code"},
    "transaction_type": {"type", "transaction type", "transaction kind"},
    "category": {"category", "expense category"},
    "source_reference": {"reference", "transaction reference", "transaction id"},
}
REQUIRED_FIELDS = {"date", "description", "amount", "currency", "transaction_type"}


def _parse_transaction_date(value: str) -> date:
    cleaned = value.strip()
    try:
        if re.match(r"^\d{4}-\d{2}-\d{2}", cleaned):
            return date.fromisoformat(cleaned[:10])
        match = re.fullmatch(r"(\d{1,2})[/-](\d{1,2})[/-](\d{4})", cleaned)
        if match:
            day, month, year = (int(part) for part in match.groups())
            return date(year, month, day)
    except ValueError as exc:
        raise ValueError("Date is not a valid supported calendar date.") from exc
    raise ValueError("Use YYYY-MM-DD or South African day-first DD/MM/YYYY dates.")


def _parse_amount(value: str, decimal_format: str, currency: str) -> Decimal:
    cleaned = value.strip().replace("\u00a0", " ")
    has_rand_symbol = bool(re.match(r"(?i)^(?:R|ZAR)\s*", cleaned))
    cleaned = re.sub(r"(?i)^(?:R|ZAR)\s*", "", cleaned)
    cleaned = re.sub(r"(?i)\s*ZAR$", "", cleaned).strip()
    cleaned = cleaned.replace(" ", "")
    if has_rand_symbol and currency != "ZAR":
        raise ValueError("Rand-prefixed amounts require currency ZAR.")

    if decimal_format == "dot":
        valid = re.fullmatch(r"[+-]?(?:\d+|\d{1,3}(?:,\d{3})+)(?:\.\d{1,2})?", cleaned)
        normalized = cleaned.replace(",", "")
    else:
        valid = re.fullmatch(r"[+-]?(?:\d+|\d{1,3}(?:\.\d{3})+)(?:,\d{1,2})?", cleaned)
        normalized = cleaned.replace(".", "").replace(",", ".")
    if not valid:
        raise ValueError(
            "Amount format is invalid or ambiguous; choose the matching decimal convention."
        )

    try:
        amount = Decimal(normalized)
    except InvalidOperation as exc:
        raise ValueError("Amount is not a valid number.") from exc
    if not amount.is_finite():
        raise ValueError("Amount must be finite.")
    if amount == 0:
        raise ValueError("Amount must not be zero.")
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


def _normalize_transaction_type(value: str) -> str:
    normalized = value.strip().lower()
    if normalized in {"revenue", "income", "sale", "sales"}:
        return "revenue"
    if normalized in {"expense", "cost", "spend", "expenditure"}:
        return "expense"
    raise ValueError("Classify each row explicitly as revenue or expense.")


def _normalize_currency(value: str) -> str:
    normalized = value.strip().upper()
    if normalized in {"R", "RAND", "RANDS"}:
        return "ZAR"
    if re.fullmatch(r"[A-Z]{3}", normalized):
        return normalized
    raise ValueError("Use an explicit three-letter currency code, such as ZAR.")


def _fingerprint(
    transaction_date: date,
    description: str,
    transaction_type: str,
    category: str,
    amount: Decimal,
    currency: str,
    source_reference: str | None,
) -> str:
    parts = (
        transaction_date.isoformat(),
        " ".join(description.casefold().split()),
        transaction_type,
        " ".join(category.casefold().split()),
        format(amount, ".2f"),
        currency,
        (source_reference or "").strip().casefold(),
    )
    return hashlib.sha256("\x1f".join(parts).encode("utf-8")).hexdigest()


def parse_financial_csv(csv_text: str, decimal_format: str) -> tuple[str, list[ParsedTransaction]]:
    if len(csv_text.encode("utf-8")) > MAX_CSV_BYTES:
        raise CSVFormatError(f"CSV file exceeds the {MAX_CSV_BYTES // 1_000_000} MB limit.")

    try:
        reader = csv.DictReader(io.StringIO(csv_text, newline=""))
        if reader.fieldnames is None:
            raise CSVFormatError("CSV must include a header row.")
        field_names: dict[str, str] = {}
        for original in reader.fieldnames:
            if not original or not original.strip():
                raise CSVFormatError("CSV header contains an empty column name.")
            normalized = _header_name(original)
            for field, aliases in HEADER_ALIASES.items():
                if normalized in aliases:
                    if field in field_names:
                        raise CSVFormatError(f"CSV has multiple columns for '{field}'.")
                    field_names[field] = original

        missing = sorted(REQUIRED_FIELDS - field_names.keys())
        if missing:
            raise CSVFormatError(
                "CSV is missing required columns: " + ", ".join(missing) + "."
            )

        rows: list[ParsedTransaction] = []
        seen_fingerprints: set[str] = set()
        for line_number, raw in enumerate(reader, start=2):
            if len(rows) >= MAX_CSV_ROWS:
                raise CSVFormatError(f"CSV exceeds the {MAX_CSV_ROWS} row limit.")
            if None in raw:
                errors = ("Row has extra fields or malformed CSV columns.",)
                rows.append(
                    ParsedTransaction(
                        line_number,
                        "invalid",
                        errors,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                    )
                )
                continue

            def value(field: str) -> str:
                column = field_names.get(field)
                return (raw.get(column) or "").strip() if column else ""

            errors: list[str] = []
            parsed_date: date | None = None
            description = value("description") or None
            transaction_type: str | None = None
            category = value("category") or "Uncategorised"
            currency: str | None = None
            amount: Decimal | None = None
            source_reference = value("source_reference") or None

            if not value("date"):
                errors.append("Date is required.")
            else:
                try:
                    parsed_date = _parse_transaction_date(value("date"))
                except ValueError as exc:
                    errors.append(str(exc))

            if not description:
                errors.append("Description is required.")
            elif len(description) > 500:
                errors.append("Description must be at most 500 characters.")
            if len(category) > 120:
                errors.append("Category must be at most 120 characters.")
            if source_reference and len(source_reference) > 255:
                errors.append("Reference must be at most 255 characters.")

            if not value("currency"):
                errors.append("Currency is required; it is not inferred.")
            else:
                try:
                    currency = _normalize_currency(value("currency"))
                except ValueError as exc:
                    errors.append(str(exc))

            if not value("transaction_type"):
                errors.append("Transaction type is required; it is not inferred from the sign.")
            else:
                try:
                    transaction_type = _normalize_transaction_type(value("transaction_type"))
                except ValueError as exc:
                    errors.append(str(exc))

            if not value("amount"):
                errors.append("Amount is required.")
            elif currency:
                try:
                    amount = _parse_amount(value("amount"), decimal_format, currency)
                except ValueError as exc:
                    errors.append(str(exc))

            fingerprint = None
            if not errors and parsed_date and description and transaction_type and currency and amount:
                fingerprint = _fingerprint(
                    parsed_date,
                    description,
                    transaction_type,
                    category,
                    amount,
                    currency,
                    source_reference,
                )
                status = "valid"
                if fingerprint in seen_fingerprints:
                    status = "duplicate"
                    errors.append("Exact duplicate row within this file; not imported twice.")
                seen_fingerprints.add(fingerprint)
            else:
                status = "invalid"

            rows.append(
                ParsedTransaction(
                    line_number,
                    status,
                    tuple(errors),
                    parsed_date,
                    description,
                    transaction_type,
                    category,
                    amount,
                    currency,
                    source_reference,
                    fingerprint,
                )
            )
    except csv.Error as exc:
        raise CSVFormatError("CSV contains malformed quoting or delimiters.") from exc

    if not rows:
        raise CSVFormatError("CSV contains no transaction rows.")
    digest = hashlib.sha256(csv_text.encode("utf-8")).hexdigest()
    return digest, rows


def mark_existing_duplicates(
    rows: list[ParsedTransaction], existing_fingerprints: set[str]
) -> list[ParsedTransaction]:
    result: list[ParsedTransaction] = []
    for row in rows:
        if row.status == "valid" and row.fingerprint in existing_fingerprints:
            result.append(
                replace(
                    row,
                    status="duplicate",
                    errors=("Exact record was imported previously; not imported twice.",),
                )
            )
        else:
            result.append(row)
    return result


def summarize_transactions(transactions: Iterable[TransactionLike]) -> dict[str, object]:
    grouped: dict[str, list[TransactionLike]] = defaultdict(list)
    transaction_count = 0
    for transaction in transactions:
        grouped[transaction.currency].append(transaction)
        transaction_count += 1

    currencies: list[dict[str, object]] = []
    for currency in sorted(grouped):
        items = grouped[currency]
        revenue = sum(
            (Decimal(transaction.amount) for transaction in items
             if transaction.transaction_type == "revenue"),
            start=Decimal("0.00"),
        )
        expenses = sum(
            (Decimal(transaction.amount) for transaction in items
             if transaction.transaction_type == "expense"),
            start=Decimal("0.00"),
        )
        net_profit = revenue - expenses
        margin = (
            (net_profit * Decimal("100") / revenue).quantize(CENT, rounding=ROUND_HALF_UP)
            if revenue > 0
            else None
        )

        period_transactions: dict[str, list[TransactionLike]] = defaultdict(list)
        category_totals: dict[str, Decimal] = defaultdict(lambda: Decimal("0.00"))
        for transaction in items:
            period_transactions[transaction.transaction_date.strftime("%Y-%m")].append(transaction)
            if transaction.transaction_type == "expense":
                category_totals[transaction.category] += Decimal(transaction.amount)

        periods: list[dict[str, object]] = []
        for period in sorted(period_transactions):
            period_items = period_transactions[period]
            period_revenue = sum(
                (
                    Decimal(item.amount)
                    for item in period_items
                    if item.transaction_type == "revenue"
                ),
                start=Decimal("0.00"),
            )
            period_expenses = sum(
                (
                    Decimal(item.amount)
                    for item in period_items
                    if item.transaction_type == "expense"
                ),
                start=Decimal("0.00"),
            )
            period_net = period_revenue - period_expenses
            period_margin = (
                (period_net * Decimal("100") / period_revenue).quantize(
                    CENT, rounding=ROUND_HALF_UP
                )
                if period_revenue > 0
                else None
            )
            periods.append(
                {
                    "period": period,
                    "revenue": period_revenue.quantize(CENT),
                    "expenses": period_expenses.quantize(CENT),
                    "net_profit": period_net.quantize(CENT),
                    "profit_margin_percent": period_margin,
                }
            )

        categories = []
        for category, category_amount in sorted(
            category_totals.items(), key=lambda item: (-item[1], item[0].casefold())
        ):
            share = (
                (category_amount * Decimal("100") / expenses).quantize(
                    CENT, rounding=ROUND_HALF_UP
                )
                if expenses > 0
                else None
            )
            categories.append(
                {
                    "category": category,
                    "amount": category_amount.quantize(CENT),
                    "share_percent": share,
                }
            )

        currencies.append(
            {
                "currency": currency,
                "revenue": revenue.quantize(CENT),
                "expenses": expenses.quantize(CENT),
                "net_profit": net_profit.quantize(CENT),
                "profit_margin_percent": margin,
                "periods": periods,
                "expense_categories": categories,
            }
        )

    return {"transaction_count": transaction_count, "currencies": currencies}


def build_evidence_and_insights(
    summary: dict[str, object],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    evidence: list[dict[str, object]] = []
    insights: list[dict[str, object]] = []
    currencies = summary["currencies"]
    assert isinstance(currencies, list)

    for currency_summary in currencies:
        assert isinstance(currency_summary, dict)
        currency = str(currency_summary["currency"])
        revenue = Decimal(currency_summary["revenue"])
        expenses = Decimal(currency_summary["expenses"])
        net_profit = Decimal(currency_summary["net_profit"])
        revenue_id = f"revenue:{currency}"
        expenses_id = f"expenses:{currency}"
        profit_id = f"net_profit:{currency}"
        evidence.extend(
            [
                {
                    "id": revenue_id,
                    "label": "Imported revenue total",
                    "value": format(revenue, ".2f"),
                    "currency": currency,
                    "period": None,
                },
                {
                    "id": expenses_id,
                    "label": "Imported expense total",
                    "value": format(expenses, ".2f"),
                    "currency": currency,
                    "period": None,
                },
                {
                    "id": profit_id,
                    "label": "Calculated net profit or loss",
                    "value": format(net_profit, ".2f"),
                    "currency": currency,
                    "period": None,
                },
            ]
        )
        if net_profit < 0:
            insights.append(
                {
                    "id": f"loss:{currency}",
                    "title": "Expenses exceed revenue",
                    "description": (
                        "The imported records show a net loss for this dataset. "
                        "Review classifications and the largest expense categories before acting."
                    ),
                    "recommended_action": (
                        "Review the imported expense categories and confirm the records "
                        "are classified correctly."
                    ),
                    "priority": "high",
                    "evidence_ids": [revenue_id, expenses_id, profit_id],
                    "origin": "deterministic",
                }
            )

        periods = currency_summary["periods"]
        assert isinstance(periods, list)
        for index in range(1, len(periods)):
            previous = periods[index - 1]
            current = periods[index]
            assert isinstance(previous, dict) and isinstance(current, dict)
            current_period = str(current["period"])
            previous_period = str(previous["period"])
            for metric, label in (("revenue", "Revenue"), ("expenses", "Expenses")):
                before = Decimal(previous[metric])
                after = Decimal(current[metric])
                is_material_direction = (
                    (metric == "revenue" and after < before)
                    or (metric == "expenses" and after > before)
                )
                if is_material_direction:
                    before_id = f"{metric}:{currency}:{previous_period}"
                    after_id = f"{metric}:{currency}:{current_period}"
                    evidence.extend(
                        [
                            {
                                "id": before_id,
                                "label": f"{label} in {previous_period}",
                                "value": format(before, ".2f"),
                                "currency": currency,
                                "period": previous_period,
                            },
                            {
                                "id": after_id,
                                "label": f"{label} in {current_period}",
                                "value": format(after, ".2f"),
                                "currency": currency,
                                "period": current_period,
                            },
                        ]
                    )
                    insights.append(
                        {
                            "id": f"{metric}_trend:{currency}:{current_period}",
                            "title": f"{label} decreased" if metric == "revenue" else f"{label} increased",
                            "description": (
                                f"Imported {label.lower()} moved in this direction from "
                                f"{previous_period} to {current_period}. This describes the "
                                "provided records and does not establish a cause."
                            ),
                            "recommended_action": (
                                f"Compare the source records for {previous_period} and "
                                f"{current_period}, then identify what changed."
                            ),
                            "priority": "medium",
                            "evidence_ids": [before_id, after_id],
                            "origin": "deterministic",
                        }
                    )

        categories = currency_summary["expense_categories"]
        assert isinstance(categories, list)
        if categories:
            largest = categories[0]
            assert isinstance(largest, dict)
            category_id = f"expense_category:{currency}:{len(evidence)}"
            evidence.append(
                {
                    "id": category_id,
                    "label": f"Largest imported expense category: {largest['category']}",
                    "value": format(Decimal(largest["amount"]), ".2f"),
                    "currency": currency,
                    "period": None,
                }
            )
            insights.append(
                {
                    "id": f"category_review:{currency}",
                    "title": "Review the largest expense category",
                    "description": (
                        f"{largest['category']} is the largest category in the imported "
                        "expense records. This is a prioritisation signal, not a finding "
                        "that the spend is unnecessary."
                    ),
                    "recommended_action": (
                        f"Review the {largest['category']} records and confirm their "
                        "business purpose and classification."
                    ),
                    "priority": "low",
                    "evidence_ids": [category_id],
                    "origin": "deterministic",
                }
            )

    return evidence, insights
