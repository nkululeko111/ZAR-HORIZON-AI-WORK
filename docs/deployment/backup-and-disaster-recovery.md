# Backup and disaster recovery

## 1. Purpose

This document describes the backup and recovery model expected for the platform. It is intentionally advisory and does not claim a final production backup policy is already implemented.

## 2. Core data categories

- transactional application data,
- documents and evidence,
- user and workspace metadata,
- audit and approval logs,
- configuration and environment metadata.

## 3. Backup requirements

- use encrypted backups,
- restrict backup access to authorised operators,
- retain backup inventory and restoration tests,
- ensure backups are consistent with the key retention model,
- document restoration process and responsibilities.

## 4. Recovery objectives

The project should define proposed recovery metrics for:

- Recovery Point Objective (RPO),
- Recovery Time Objective (RTO),
- restoration prioritisation,
- recovery procedures for each service or data set.

These values are not final and still require founder approval.

## 5. Recovery testing

Operational teams should run periodic restoration exercises to validate the backup process, including:

- database restore rehearsal,
- document/evidence restore rehearsal,
- permission verification after restore,
- audit log integrity checks.

## 6. Recommendation

The repo should continue to recommend prudent, reviewable backup and recovery controls without prematurely selecting a final production architecture or hosting model.
