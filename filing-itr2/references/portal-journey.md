# Portal journey

## Operating loop

For every portal screen:

1. Ask the user to attach a screenshot of the current screen.
2. Identify the screen and compare visible values with the evidence ledger.
3. Explain why the next field matters.
4. Give exactly one action or one focused question.
5. Wait for the next screenshot.
6. Record what was confirmed and what remains open.

Do not give a long sequence of clicks unless the user explicitly requests it.
Never infer that a hidden, collapsed, disabled, or off-screen field is correct.

## Suggested schedule order

Use the current portal's schedule list; labels and dependencies can change.

1. Part A – General: filing section, regime, residential status, bank accounts.
2. Salary, House Property, Capital Gains, Schedule 112A, Other Sources.
3. Chapter VI-A and detailed deduction schedules.
4. CYLA, BFLA, CFL and Schedule SI.
5. Tax Paid.
6. Part B-TI and Part B-TTI.

Select only relevant optional schedules. Mandatory computed schedules may remain
selected with zero values.

## Dependency rule

After changing an upstream schedule, return to the summary and re-open/reconfirm
every dependent computed schedule. Typical examples:

- CG change → Schedule SI, CYLA, BFLA, CFL, Part B-TI, Part B-TTI.
- HP change → CYLA, BFLA, Part B-TI, Part B-TTI.
- OS or VIA change → CYLA where relevant, Part B-TI, Part B-TTI.
- Tax Paid change → Part B-TTI.

## Screen-level safeguards

- Translate portal wording into plain language; do not ask the user to interpret
  section numbers.
- If a field is disabled, find its source schedule instead of forcing a value.
- Treat gross sale value, capital gain, taxable gain, deduction, and set-off as
  different quantities.
- When the portal auto-populates a set-off, verify the row/column headers and
  final totals before confirming.
- If validation opens a field, fix the classification at its source rather than
  entering a convenient value to silence the error.
- Stop when the evidence and portal cannot be reconciled. Describe the mismatch,
  source documents, and estimated tax effect.

## User-controlled actions

The user logs in, handles CAPTCHA/password/OTP, authorizes tax payment, clicks
final Submit, and performs e-verification. The agent may explain the result and
check the evidence afterwards, but must not impersonate the filer.
