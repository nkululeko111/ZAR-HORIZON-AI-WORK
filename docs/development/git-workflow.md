# Git branching and contribution standards

## 1. Purpose

This document defines a simple, practical Git workflow for the repository. The goal is to keep the project maintainable without introducing unnecessary process overhead.

## 2. Branch model

### `main`

`main` is the stable integration branch and should contain reviewed, releasable work.

### Feature branches

Use short-lived feature branches for work in progress.

Suggested naming:

- `feature/<short-name>`
- `fix/<short-name>`
- `docs/<short-name>`
- `chore/<short-name>`

### Bug-fix branches

Use a dedicated bug-fix branch when fixing issues or regressions.

### Urgent security fixes

Urgent security or safety fixes should be handled with the shortest possible review path while still requiring a pull request and explicit review when feasible. The repository should not rely on direct pushes to `main` for sensitive or high-risk changes.

## 3. Pull request expectations

All work should be reviewed before merging into `main`.

Minimum expectations:

- clear summary of the change,
- impact scope,
- validation performed,
- any assumptions or follow-up needed,
- reviewer sign-off from the relevant owner.

For cross-product changes, both the shared platform and affected product owners should be included in review where relevant.

## 4. Commit standards

Use concise, descriptive commit messages.

Recommended pattern:

- `feat: add shared platform onboarding docs`
- `fix: correct docker env variable naming`
- `docs: add developer onboarding workflow`
- `chore: update repo development standards`

Keep commits focused and avoid mixing unrelated product work into one change.

## 5. Review expectations

- keep PRs small and targeted,
- include relevant technical and documentation context,
- validate the change with the minimum relevant command,
- make sure changes affecting both products or shared infra are reviewed carefully.

## 6. Branch protection guidance

The repository should follow GitHub branch protection for `main` as a policy decision, but actual branch settings are not configured in this exercise and should not be changed without explicit approval.

## 7. Summary

This is intentionally a lightweight Git workflow: one stable branch, short-lived feature branches, pull requests, clear commit conventions, and a sensible review model for platform and product changes.
