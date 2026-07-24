# ITR-2 Filing Skills Design

## Objective

Create a reusable, public-safe pair of skills that guide an individual through
Indian ITR-2 preparation, portal entry, verification, and acknowledgement
review. The experience must help the user remain compliant and claim every
lawful tax benefit without turning the interaction into a long tax form.

## Product principles

1. Ask one focused question or request one action at a time.
2. Infer answers from attached documents before asking the user.
3. Explain why a question matters in one plain-language sentence.
4. Tailor document collection to the user's actual income and deduction profile.
5. Separate facts, calculations, and unresolved decisions.
6. Verify mutable rules for the selected assessment year from official sources.
7. Reconcile portal prefill, user documents, and computations; never trust one
   automatically.
8. Stop at defined checkpoints for user review, payment, submission, OTP, and
   e-verification.
9. Never include real taxpayer data, screenshots, identifiers, or documents in
   the shared skill.

## Architecture

The repository contains two independently discoverable skills:

- `filing-itr2`: the base journey for individual ITR-2 filers.
- `filing-itr2-nri`: an extension loaded with the base skill when foreign
  residence or non-resident status is relevant.

The preparation architecture is inspired by the source-ledger, live-rule
verification, and schedule-reconciliation patterns in
[`NidheeshJain/itr-prep-skill`](https://github.com/NidheeshJain/itr-prep-skill).
This implementation narrows the scope to ITR-2 and adds the guided portal,
preview-PDF, acknowledgement, and NRI evidence journeys.

The base skill owns the common journey:

1. Establish FY/AY and provisional ITR eligibility.
2. Build a tailored document checklist.
3. Reconcile AIS/TIS/26AS and source documents.
4. Compare regimes using computed figures.
5. Build a schedule map and guide portal entry one screen at a time.
6. Reconcile the preview PDF.
7. Review the acknowledgement and explain tax payable/refund and verification
   status.

The NRI extension adds:

- Indian day-count and residency determination.
- Foreign tax jurisdiction, foreign TIN, and TRC readiness.
- NRI-specific portal questions and treaty evidence.
- ROR/RNOR/NR foreign-asset and foreign-income distinctions.

## Guardrails learned from the reference filing

- Require all broker/demat Tax P&L reports before entering capital gains.
- Distinguish quoted equity, equity-oriented funds, debt/non-equity funds,
  unquoted shares, and other assets before selecting a portal field.
- Treat Section 54F as an eligibility and chronology workflow, not a number to
  enter blindly.
- Reconfirm dependent schedules after upstream changes.
- Audit the preview PDF and acknowledgement rather than stopping at portal
  validation.

## Out of scope

- Filing returns with business/professional income that require ITR-3.
- Handling credentials, passwords, OTPs, payment authorization, or final
  submission on the user's behalf.
- Guaranteeing a tax position where facts or law are uncertain.
- Replacing a chartered accountant for audit, notice, contested residency,
  complex treaty, or high-risk valuation cases.
