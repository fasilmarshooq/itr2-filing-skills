---
name: filing-itr2-nri
description: Use when an Indian ITR-2 filer lives, works, pays tax, holds residency, or spends substantial time outside India; identifies as NRI/RNOR; has a foreign tax jurisdiction or TIN; may need a TRC, Form 10F, or DTAA position; or needs help with NRI-specific ITR-2 portal questions.
---

# Filing ITR-2 for an NRI

Add the smallest necessary NRI layer to the common filing journey.

**REQUIRED BASE SKILL:** Use `filing-itr2` for document reconciliation, regime
comparison, capital gains, portal entry, preview review, and acknowledgement
review. Do not repeat that questionnaire here.

## Interaction rule

Continue the base skill's one-question-at-a-time journey. Ask first for facts
that can change Indian residential status, then request treaty evidence only if
it could affect an actual income item. Explain the consequence briefly.

## NRI sequence

1. Read `references/nri-residency-and-treaty.md`.
2. Build a dated presence record from travel evidence and determine the
   residential-status basis using current official law.
3. Record foreign tax jurisdiction, foreign taxpayer identification number,
   and tax-residency evidence.
4. Classify each income item by source and Indian tax treatment. Location of a
   bank account or non-repatriation of money does not decide taxability.
5. Determine whether any DTAA position is beneficial and sufficiently
   documented. Show domestic-law and treaty outcomes separately.
6. Read `references/nri-portal-checks.md` during portal entry.
7. Carry the residential-status basis, treaty evidence, and unresolved warnings
   into the preview-PDF review.

## Safety

Browse official Indian sources and the relevant treaty text for the selected
AY. Do not invent residency days, treaty articles, rates, TINs, TRC status, or
FPI status. Do not claim treaty relief merely because the user is tax-resident
abroad. Escalate contested dual residence, tie-breaker analysis, permanent
establishment, complex foreign tax credit, or missing evidence with material
tax impact.
