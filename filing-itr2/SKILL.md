---
name: filing-itr2
description: Use when an individual needs help preparing, entering, reviewing, or verifying an Indian ITR-2; choosing an ITR form or tax regime where capital gains, multiple properties, foreign assets, carried losses, dividends, interest, AIS, 26AS, broker Tax P&L, a portal preview PDF, or an ITR acknowledgement may be involved.
---

# Filing ITR-2

Guide the user to report required income and claim lawful, evidenced benefits.

## Interaction contract

- Ask one focused question or request one action at a time. Wait for the answer.
- Infer facts from attached documents before asking.
- Explain why the question matters in one plain-language sentence.
- Request only evidence relevant to the user's profile.
- Keep a short progress recap: `Collected`, `Verified`, `Missing`, `Next`.
- Frame deductions as lawful savings, never hidden income.

## Authority and safety

Confirm the financial year and assessment year. Browse official Income Tax
Department material on `incometax.gov.in` or `incometaxindia.gov.in` before
using a mutable rate, limit, date, eligibility rule, portal label, or deadline.
Cite it near the decision. Use third-party sites only as explanations.

Never handle a password or OTP, authorize payment, click final Submit, or
complete e-verification. Stop for a CA on business/professional income, audits,
notices, contested residency, unsupported valuation, or uncertain treaties.

If foreign residence or NRI/RNOR status is possible, **REQUIRED SUB-SKILL:** use
`filing-itr2-nri` with this skill.

## Journey

### 1. Establish scope

Confirm AY, filing status, income sources, prior losses, and goal. Check ITR-2
eligibility; route business, freelance, F&O, or intraday-business elsewhere.

### 2. Become filing-ready

Read `references/intake-and-reconciliation.md`. Build a tailored checklist and
collect one missing source at a time. Reconcile an evidence ledger:

`source document → fact/amount → calculation → ITR schedule → status`

Do not start portal entry while a material income, tax-credit, residency, or
capital-gain classification blocker remains.

### 3. Compute and save tax lawfully

Compare regimes from the ledger and explain the difference. Present savings in
three groups:

- `Supported now` — evidence and eligibility verified; include in computation.
- `Needs evidence` — potentially eligible; request the one missing proof next.
- `Not eligible` — exclude and explain the reason briefly.

Recommend the lower compliant result, never an unsupported claim. For capital
gains or a house purchase, read
`references/capital-gains-and-exemptions.md`.

### 4. Enter the portal

Read `references/portal-journey.md`. Ask for the current screenshot, explain it,
give one action, then request the next screenshot. Reconcile prefill against
evidence; neither automatically wins. Reconfirm dependent schedules after edits.

### 5. Verify before filing

Ask for the preview PDF and read `references/preview-and-ack-review.md`.
Reconcile material figures, show tax payable/refund, and stop before payment or
submission for approval.

### 6. Verify after filing

Ask for the acknowledgement. Confirm filing section, total income, tax/refund,
submission date, verification status, and any deadline. Never infer that a
return is filed merely because portal validation succeeded.
