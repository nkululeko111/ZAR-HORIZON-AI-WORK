'use client';

import { useCallback, useEffect, useState } from 'react';
import type { FormEvent } from 'react';

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

type BusinessProfile = {
  id: string;
  business_name: string;
  business_type: string | null;
  industry: string | null;
  country: string;
  currency_code: string;
  region: string | null;
};

type FinancialPeriod = {
  period: string;
  revenue: string;
  expenses: string;
  net_profit: string;
  profit_margin_percent: string | null;
};

type ExpenseCategory = {
  category: string;
  amount: string;
  share_percent: string | null;
};

type CurrencySummary = {
  currency: string;
  revenue: string;
  expenses: string;
  net_profit: string;
  profit_margin_percent: string | null;
  periods: FinancialPeriod[];
  expense_categories: ExpenseCategory[];
};

type FinancialSummary = {
  transaction_count: number;
  currencies: CurrencySummary[];
  latest_import_at: string | null;
};

type PreviewRow = {
  line_number: number;
  status: 'valid' | 'invalid' | 'duplicate';
  errors: string[];
  transaction_date: string | null;
  description: string | null;
  transaction_type: 'revenue' | 'expense' | null;
  category: string | null;
  amount: string | null;
  currency: string | null;
};

type CsvPreview = {
  file_duplicate: boolean;
  rows: PreviewRow[];
  valid_count: number;
  invalid_count: number;
  duplicate_count: number;
  imported_count?: number | null;
};

type Evidence = {
  id: string;
  label: string;
  value: string;
  currency: string | null;
  period: string | null;
};

type Insight = {
  id: string;
  title: string;
  description: string;
  recommended_action: string;
  priority: 'low' | 'medium' | 'high';
  evidence_ids: string[];
  origin: 'deterministic' | 'ai';
};

type Analysis = {
  analysis_id: string;
  ai_status: 'not_configured' | 'not_available' | 'available';
  ai_message: string;
  summary: string;
  summary_evidence_ids: string[];
  answer: string | null;
  answer_evidence_ids: string[];
  deterministic_insights: Insight[];
  ai_insights: Insight[];
  evidence: Evidence[];
};

type BusinessAction = {
  id: string;
  analysis_id: string;
  source_insight_id: string;
  title: string;
  description: string;
  reason: string;
  priority: 'low' | 'medium' | 'high';
  status: 'open' | 'in_progress' | 'completed' | 'cancelled';
  outcome: string | null;
  external_execution_status: 'not_executed';
  supporting_evidence: Evidence[];
  created_at: string;
  completed_at: string | null;
};

type ProfileForm = {
  business_name: string;
  business_type: string;
  industry: string;
  country: string;
  currency_code: string;
  region: string;
};

const emptyProfile: ProfileForm = {
  business_name: '',
  business_type: '',
  industry: '',
  country: 'ZA',
  currency_code: 'ZAR',
  region: '',
};

async function apiRequest<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_URL}${path}`, {
    ...init,
    cache: 'no-store',
    headers: {
      'Content-Type': 'application/json',
      ...init?.headers,
    },
  });
  const responseText = await response.text();
  let responseBody: unknown;
  if (responseText) {
    try {
      responseBody = JSON.parse(responseText);
    } catch {
      if (response.ok) {
        throw new Error('The API returned an invalid response.');
      }
    }
  }
  if (!response.ok) {
    const detail =
      typeof responseBody === 'object' &&
      responseBody !== null &&
      'detail' in responseBody &&
      typeof responseBody.detail === 'string'
        ? responseBody.detail
        : `Request failed with status ${response.status}.`;
    throw new Error(detail);
  }
  return responseBody as T;
}

function formatCurrency(value: string, currency: string): string {
  const amount = Number(value);
  if (!Number.isFinite(amount)) return `${value} ${currency}`;
  return new Intl.NumberFormat('en-ZA', {
    style: 'currency',
    currency,
    maximumFractionDigits: 2,
  }).format(amount);
}

function getErrorMessage(error: unknown): string {
  return error instanceof Error ? error.message : 'An unexpected error occurred.';
}

export default function BusinessPartnerPage() {
  const [profile, setProfile] = useState<BusinessProfile | null>(null);
  const [editingProfile, setEditingProfile] = useState(false);
  const [profileForm, setProfileForm] = useState<ProfileForm>(emptyProfile);
  const [summary, setSummary] = useState<FinancialSummary | null>(null);
  const [actions, setActions] = useState<BusinessAction[]>([]);
  const [preview, setPreview] = useState<CsvPreview | null>(null);
  const [fileName, setFileName] = useState('');
  const [csvText, setCsvText] = useState('');
  const [decimalFormat, setDecimalFormat] = useState<'dot' | 'comma'>('dot');
  const [question, setQuestion] = useState('');
  const [analysis, setAnalysis] = useState<Analysis | null>(null);
  const [actionOutcomes, setActionOutcomes] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [notice, setNotice] = useState<string | null>(null);

  const loadWorkspace = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const currentProfile = await apiRequest<BusinessProfile>('/api/v1/business/profile');
      setProfile(currentProfile);
      setProfileForm({
        business_name: currentProfile.business_name,
        business_type: currentProfile.business_type ?? '',
        industry: currentProfile.industry ?? '',
        country: currentProfile.country,
        currency_code: currentProfile.currency_code,
        region: currentProfile.region ?? '',
      });
      const [currentSummary, currentActions] = await Promise.all([
        apiRequest<FinancialSummary>('/api/v1/business/financial/summary'),
        apiRequest<BusinessAction[]>('/api/v1/business/actions'),
      ]);
      setSummary(currentSummary);
      setActions(currentActions);
    } catch (loadError) {
      if (loadError instanceof Error && loadError.message === 'No business profile has been created yet.') {
        setProfile(null);
        setSummary(null);
        setActions([]);
        setError(null);
      } else {
        setError(getErrorMessage(loadError));
      }
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    void loadWorkspace();
  }, [loadWorkspace]);

  async function saveProfile(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy('profile');
    setError(null);
    setNotice(null);
    try {
      const saved = await apiRequest<BusinessProfile>('/api/v1/business/profile', {
        method: 'POST',
        body: JSON.stringify(profileForm),
      });
      setProfile(saved);
      setEditingProfile(false);
      setNotice('Business profile saved.');
      await loadWorkspace();
    } catch (saveError) {
      setError(getErrorMessage(saveError));
    } finally {
      setBusy(null);
    }
  }

  async function selectCsv(file: File | undefined) {
    setPreview(null);
    setCsvText('');
    setFileName('');
    setError(null);
    setNotice(null);
    if (!file) return;
    if (!file.name.toLowerCase().endsWith('.csv')) {
      setError('Choose a CSV file.');
      return;
    }
    try {
      const contents = await file.text();
      setFileName(file.name);
      setCsvText(contents);
    } catch {
      setError('The selected CSV file could not be read.');
    }
  }

  async function previewCsv(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy('preview');
    setError(null);
    setNotice(null);
    try {
      const result = await apiRequest<CsvPreview>('/api/v1/business/financial/import/preview', {
        method: 'POST',
        body: JSON.stringify({ file_name: fileName, csv_text: csvText, decimal_format: decimalFormat }),
      });
      setPreview(result);
      setNotice('Preview complete. Review every row before importing.');
    } catch (previewError) {
      setError(getErrorMessage(previewError));
    } finally {
      setBusy(null);
    }
  }

  async function importCsv() {
    if (!fileName || !csvText) return;
    setBusy('import');
    setError(null);
    setNotice(null);
    try {
      const result = await apiRequest<CsvPreview>('/api/v1/business/financial/import', {
        method: 'POST',
        body: JSON.stringify({ file_name: fileName, csv_text: csvText, decimal_format: decimalFormat }),
      });
      setPreview(result);
      setNotice(`${result.imported_count ?? 0} validated rows imported. Duplicate and invalid rows were skipped.`);
      await refreshSummaryAndActions();
    } catch (importError) {
      setError(getErrorMessage(importError));
    } finally {
      setBusy(null);
    }
  }

  async function refreshSummaryAndActions() {
    const [currentSummary, currentActions] = await Promise.all([
      apiRequest<FinancialSummary>('/api/v1/business/financial/summary'),
      apiRequest<BusinessAction[]>('/api/v1/business/actions'),
    ]);
    setSummary(currentSummary);
    setActions(currentActions);
  }

  async function analyse(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy('analysis');
    setError(null);
    setNotice(null);
    try {
      const result = await apiRequest<Analysis>('/api/v1/business/analysis', {
        method: 'POST',
        body: JSON.stringify({ question: question.trim() || null }),
      });
      setAnalysis(result);
      setNotice('Analysis is based on the validated financial records shown below.');
    } catch (analysisError) {
      setError(getErrorMessage(analysisError));
    } finally {
      setBusy(null);
    }
  }

  async function createAction(insight: Insight) {
    if (!analysis) return;
    setBusy(`action-${insight.id}`);
    setError(null);
    setNotice(null);
    try {
      await apiRequest<BusinessAction>('/api/v1/business/actions', {
        method: 'POST',
        body: JSON.stringify({
          analysis_id: analysis.analysis_id,
          insight_id: insight.id,
        }),
      });
      await refreshSummaryAndActions();
      setNotice('Recommendation added to internal action tracking; no external action was executed.');
    } catch (actionError) {
      setError(getErrorMessage(actionError));
    } finally {
      setBusy(null);
    }
  }

  async function updateAction(action: BusinessAction, status: BusinessAction['status']) {
    setBusy(`update-${action.id}`);
    setError(null);
    setNotice(null);
    try {
      const updated = await apiRequest<BusinessAction>(`/api/v1/business/actions/${action.id}`, {
        method: 'PATCH',
        body: JSON.stringify({
          status,
          outcome: status === 'completed' ? actionOutcomes[action.id]?.trim() || null : null,
        }),
      });
      setActions((current) => current.map((item) => (item.id === updated.id ? updated : item)));
      setNotice(
        status === 'completed'
          ? 'Internal action marked complete. This does not indicate external execution.'
          : 'Action status updated.',
      );
    } catch (updateError) {
      setError(getErrorMessage(updateError));
    } finally {
      setBusy(null);
    }
  }

  const allInsights = analysis
    ? [...analysis.deterministic_insights, ...analysis.ai_insights]
    : [];
  const evidenceById = new Map((analysis?.evidence ?? []).map((item) => [item.id, item]));

  return (
    <main className="workspace-page">
      <header className="workspace-header">
        <a className="workspace-back" href="/">
          ← ZAR HORIZON AI @WORK
        </a>
        <span className="local-badge">LOCAL DEVELOPMENT WORKSPACE</span>
      </header>

      <section className="workspace-intro">
        <p className="eyebrow">AI BUSINESS PARTNER · PERFORMANCE INTELLIGENCE</p>
        <h1>Know the numbers.<br /><span>Choose what&apos;s next.</span></h1>
        <p>
          Import your own classified financial records, review deterministic calculations and
          explore evidence-backed recommendations. No sample customer data is shown.
        </p>
      </section>

      <div className="workspace-notice" role="note">
        Development-only, single local workspace. Authentication and multi-tenant access control
        are not implemented. Do not use real or sensitive financial data.
      </div>
      {error && <div className="feedback error" role="alert">{error}</div>}
      {notice && <div className="feedback success" role="status">{notice}</div>}

      {loading ? (
        <p className="workspace-loading" role="status">Loading Business Partner workspace…</p>
      ) : error ? (
        <section className="panel connection-panel">
          <h2>Workspace unavailable</h2>
          <p>Check that the local API, database and migrations are running, then retry.</p>
          <button className="button secondary" onClick={() => void loadWorkspace()} type="button">
            Retry connection
          </button>
        </section>
      ) : !profile || editingProfile ? (
        <section className="panel profile-panel">
          <div className="panel-heading">
            <div>
              <p className="eyebrow">{profile ? 'BUSINESS PROFILE' : 'FIRST STEP'}</p>
              <h2>{profile ? 'Update your business profile' : 'Create your business profile'}</h2>
            </div>
            <span className="step-count">{profile ? 'EDIT' : '01 / 04'}</span>
          </div>
          <p className="muted">
            This profile is stored in the local development database and helps label your workspace.
          </p>
          <form className="profile-form" onSubmit={saveProfile}>
            <label>
              Business name <span aria-hidden="true">*</span>
              <input
                autoComplete="organization"
                maxLength={200}
                onChange={(event) => setProfileForm({ ...profileForm, business_name: event.target.value })}
                required
                value={profileForm.business_name}
              />
            </label>
            <label>
              Business type
              <input
                maxLength={120}
                onChange={(event) => setProfileForm({ ...profileForm, business_type: event.target.value })}
                placeholder="For example, independent retailer"
                value={profileForm.business_type}
              />
            </label>
            <label>
              Industry
              <input
                maxLength={120}
                onChange={(event) => setProfileForm({ ...profileForm, industry: event.target.value })}
                value={profileForm.industry}
              />
            </label>
            <label>
              Region
              <input
                maxLength={120}
                onChange={(event) => setProfileForm({ ...profileForm, region: event.target.value })}
                placeholder="Province or city"
                value={profileForm.region}
              />
            </label>
            <label>
              Country code
              <input
                maxLength={2}
                onChange={(event) => setProfileForm({ ...profileForm, country: event.target.value })}
                required
                value={profileForm.country}
              />
            </label>
            <label>
              Primary currency
              <input
                maxLength={3}
                onChange={(event) =>
                  setProfileForm({ ...profileForm, currency_code: event.target.value })
                }
                required
                value={profileForm.currency_code}
              />
            </label>
            <button className="button primary" disabled={busy === 'profile'} type="submit">
              {busy === 'profile' ? 'Saving…' : profile ? 'Save changes' : 'Save business profile'}
            </button>
            {profile && (
              <button
                className="button secondary"
                onClick={() => setEditingProfile(false)}
                type="button"
              >
                Cancel
              </button>
            )}
          </form>
        </section>
      ) : (
        <>
          <section className="workspace-business-heading">
            <div>
              <p className="eyebrow">YOUR LOCAL BUSINESS PROFILE</p>
              <h2>{profile.business_name}</h2>
              <p className="muted">
                {[profile.business_type, profile.industry, profile.region].filter(Boolean).join(' · ') ||
                  'Profile saved'}
              </p>
            </div>
            <button className="text-button" onClick={() => setEditingProfile(true)} type="button">
              Edit profile
            </button>
          </section>
          <div className="workspace-grid">
              <section className="panel import-panel">
                <div className="panel-heading">
                  <div>
                    <p className="eyebrow">01 · IMPORT</p>
                    <h2>Bring your financial data</h2>
                  </div>
                  <span className="step-count">CSV</span>
                </div>
                <p className="muted">
                  Required columns: date, description, amount, currency and type (revenue or expense).
                  Category is optional. Records are not classified automatically.
                </p>
                <form onSubmit={previewCsv}>
                  <label className="file-picker">
                    <span>Choose a CSV file</span>
                    <input
                      accept=".csv,text/csv"
                      onChange={(event) => void selectCsv(event.target.files?.[0])}
                      type="file"
                    />
                  </label>
                  {fileName && <p className="selected-file">Selected: {fileName}</p>}
                  <label className="select-label">
                    Amount decimal convention
                    <select
                      onChange={(event) => setDecimalFormat(event.target.value as 'dot' | 'comma')}
                      value={decimalFormat}
                    >
                      <option value="dot">Dot decimal (1,234.56)</option>
                      <option value="comma">Comma decimal (1.234,56)</option>
                    </select>
                  </label>
                  <button
                    className="button primary"
                    disabled={!fileName || busy === 'preview' || !csvText}
                    type="submit"
                  >
                    {busy === 'preview' ? 'Validating…' : 'Preview and validate'}
                  </button>
                </form>
                {preview && (
                  <div className="preview-results">
                    <div className="preview-counts" aria-live="polite">
                      <span>{preview.valid_count} valid</span>
                      <span>{preview.invalid_count} invalid</span>
                      <span>{preview.duplicate_count} duplicate</span>
                    </div>
                    <div className="table-scroll">
                      <table>
                        <thead>
                          <tr><th>Line</th><th>Status</th><th>Date / description</th><th>Type</th><th>Amount</th><th>Validation</th></tr>
                        </thead>
                        <tbody>
                          {preview.rows.map((row) => (
                            <tr key={row.line_number}>
                              <td>{row.line_number}</td>
                              <td><span className={`row-status ${row.status}`}>{row.status}</span></td>
                              <td>{row.transaction_date ?? '—'}<br />{row.description ?? '—'}</td>
                              <td>{row.transaction_type ?? '—'}</td>
                              <td>{row.amount && row.currency ? formatCurrency(row.amount, row.currency) : '—'}</td>
                              <td>{row.errors.length ? row.errors.join(' ') : 'Ready to import'}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                    <button
                      className="button primary"
                      disabled={preview.file_duplicate || preview.valid_count === 0 || busy === 'import'}
                      onClick={() => void importCsv()}
                      type="button"
                    >
                      {busy === 'import' ? 'Importing…' : 'Import valid unique rows'}
                    </button>
                    {preview.file_duplicate && <p className="muted">This exact file was imported previously.</p>}
                  </div>
                )}
              </section>

              <section className="panel summary-panel">
                <div className="panel-heading">
                  <div>
                    <p className="eyebrow">02 · PERFORMANCE</p>
                    <h2>Financial summary</h2>
                  </div>
                  <span className="step-count">{summary?.transaction_count ?? 0} records</span>
                </div>
                {!summary || summary.transaction_count === 0 ? (
                  <div className="empty-state">
                    <strong>No validated financial records yet.</strong>
                    <p>Import a CSV to see revenue, expenses and period-by-period performance.</p>
                  </div>
                ) : (
                  <div className="currency-summaries">
                    {summary.currencies.map((currency) => (
                      <article className="currency-summary" key={currency.currency}>
                        <h3>{currency.currency} performance</h3>
                        <div className="metric-grid">
                          <div><span>Revenue</span><strong>{formatCurrency(currency.revenue, currency.currency)}</strong></div>
                          <div><span>Expenses</span><strong>{formatCurrency(currency.expenses, currency.currency)}</strong></div>
                          <div><span>Net profit / loss</span><strong>{formatCurrency(currency.net_profit, currency.currency)}</strong></div>
                          <div><span>Profit margin</span><strong>{currency.profit_margin_percent === null ? 'Not applicable' : `${currency.profit_margin_percent}%`}</strong></div>
                        </div>
                        <h4>Reporting periods</h4>
                        <div className="table-scroll">
                          <table>
                            <thead><tr><th>Period</th><th>Revenue</th><th>Expenses</th><th>Net</th><th>Margin</th></tr></thead>
                            <tbody>
                              {currency.periods.map((period) => (
                                <tr key={period.period}>
                                  <td>{period.period}</td>
                                  <td>{formatCurrency(period.revenue, currency.currency)}</td>
                                  <td>{formatCurrency(period.expenses, currency.currency)}</td>
                                  <td>{formatCurrency(period.net_profit, currency.currency)}</td>
                                  <td>{period.profit_margin_percent === null ? '—' : `${period.profit_margin_percent}%`}</td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                        </div>
                        <h4>Expense categories</h4>
                        {currency.expense_categories.length ? (
                          <ul className="category-list">
                            {currency.expense_categories.map((category) => (
                              <li key={category.category}>
                                <span>{category.category} {category.share_percent !== null && <small>{category.share_percent}%</small>}</span>
                                <strong>{formatCurrency(category.amount, currency.currency)}</strong>
                              </li>
                            ))}
                          </ul>
                        ) : <p className="muted">No expense categories in these records.</p>}
                      </article>
                    ))}
                  </div>
                )}
              </section>

              <section className="panel intelligence-panel">
                <div className="panel-heading">
                  <div>
                    <p className="eyebrow">03 · INTERPRET</p>
                    <h2>Ask about your business</h2>
                  </div>
                  <span className="step-count">EVIDENCE FIRST</span>
                </div>
                <p className="muted">
                  Calculations are deterministic. AI is optional and receives validated summaries,
                  not transaction-level descriptions. No AI response is shown when a provider is unavailable.
                </p>
                <form className="question-form" onSubmit={analyse}>
                  <label htmlFor="business-question">Question (optional)</label>
                  <textarea
                    id="business-question"
                    maxLength={1000}
                    onChange={(event) => setQuestion(event.target.value)}
                    placeholder="For example: What should I review in this period?"
                    rows={3}
                    value={question}
                  />
                  <button className="button primary" disabled={busy === 'analysis'} type="submit">
                    {busy === 'analysis' ? 'Analysing…' : 'Analyse validated data'}
                  </button>
                </form>
                {analysis && (
                  <div className="analysis-results">
                    <p className={`ai-state ${analysis.ai_status}`}>
                      {analysis.ai_status === 'available' ? 'AI provider connected' :
                        analysis.ai_status === 'not_configured' ? 'AI not configured' : 'Analysis unavailable'}
                    </p>
                    <p>{analysis.ai_message}</p>
                    <h3>Performance explanation</h3>
                    <p>{analysis.summary}</p>
                    <EvidenceList ids={analysis.summary_evidence_ids} evidenceById={evidenceById} />
                    {analysis.answer && (
                      <>
                        <h3>Your answer</h3>
                        <p>{analysis.answer}</p>
                        <EvidenceList ids={analysis.answer_evidence_ids} evidenceById={evidenceById} />
                      </>
                    )}
                    {allInsights.length === 0 ? (
                      <div className="empty-state">
                        No material trend or risk was identified from the imported records. This does
                        not establish that the business has no issues.
                      </div>
                    ) : (
                      <div className="insight-list">
                        {allInsights.map((insight) => (
                          <article className="insight-card" key={insight.id}>
                            <div className="insight-heading">
                              <h3>{insight.title}</h3>
                              <span className={`priority ${insight.priority}`}>{insight.priority} priority</span>
                            </div>
                            <p>{insight.description}</p>
                            <p><strong>Suggested next step:</strong> {insight.recommended_action}</p>
                            <EvidenceList ids={insight.evidence_ids} evidenceById={evidenceById} />
                            <button
                              className="button secondary"
                              disabled={busy === `action-${insight.id}`}
                              onClick={() => void createAction(insight)}
                              type="button"
                            >
                              {busy === `action-${insight.id}` ? 'Adding…' : 'Track this action'}
                            </button>
                          </article>
                        ))}
                      </div>
                    )}
                  </div>
                )}
              </section>

              <section className="panel actions-panel">
                <div className="panel-heading">
                  <div>
                    <p className="eyebrow">04 · FOLLOW THROUGH</p>
                    <h2>Action tracking</h2>
                  </div>
                  <span className="step-count">{actions.length} tracked</span>
                </div>
                <p className="muted">
                  These are internal tasks only. Completing a task records your outcome; it does not
                  execute an action in another system.
                </p>
                {actions.length === 0 ? (
                  <div className="empty-state">No actions tracked yet. Add one from a supported insight.</div>
                ) : (
                  <div className="action-list">
                    {actions.map((action) => (
                      <article className="action-card" key={action.id}>
                        <div className="insight-heading">
                          <h3>{action.title}</h3>
                          <span className={`action-status ${action.status}`}>{action.status.replace('_', ' ')}</span>
                        </div>
                        <p>{action.description}</p>
                        <p className="muted">{action.reason}</p>
                        <EvidenceList
                          ids={action.supporting_evidence.map((item) => item.id)}
                          evidenceById={new Map(action.supporting_evidence.map((item) => [item.id, item]))}
                        />
                        <small>External execution: not executed · Created {new Date(action.created_at).toLocaleDateString('en-ZA')}</small>
                        {action.outcome && <p><strong>Recorded outcome:</strong> {action.outcome}</p>}
                        {action.status !== 'completed' && action.status !== 'cancelled' && (
                          <div className="action-controls">
                            <label>
                              Completion outcome
                              <input
                                onChange={(event) =>
                                  setActionOutcomes({ ...actionOutcomes, [action.id]: event.target.value })
                                }
                                placeholder="Required to complete"
                                value={actionOutcomes[action.id] ?? ''}
                              />
                            </label>
                            <div>
                              <button
                                className="button secondary"
                                disabled={busy === `update-${action.id}`}
                                onClick={() => void updateAction(action, 'in_progress')}
                                type="button"
                              >
                                Start
                              </button>
                              <button
                                className="button primary"
                                disabled={
                                  busy === `update-${action.id}` ||
                                  !(actionOutcomes[action.id] ?? '').trim()
                                }
                                onClick={() => void updateAction(action, 'completed')}
                                type="button"
                              >
                                Mark complete
                              </button>
                              <button
                                className="text-button"
                                disabled={busy === `update-${action.id}`}
                                onClick={() => void updateAction(action, 'cancelled')}
                                type="button"
                              >
                                Cancel
                              </button>
                            </div>
                          </div>
                        )}
                      </article>
                    ))}
                  </div>
                )}
              </section>
          </div>
        </>
      )}
    </main>
  );
}

function EvidenceList({
  ids,
  evidenceById,
}: {
  ids: string[];
  evidenceById: Map<string, Evidence>;
}) {
  const entries = ids.map((id) => evidenceById.get(id)).filter((item): item is Evidence => Boolean(item));
  if (entries.length === 0) return null;
  return (
    <ul className="evidence-list" aria-label="Supporting evidence">
      {entries.map((item) => (
        <li key={item.id}>
          <span>{item.label}{item.period ? ` · ${item.period}` : ''}</span>
          <strong>{item.currency ? formatCurrency(item.value, item.currency) : item.value}</strong>
        </li>
      ))}
    </ul>
  );
}
