# ITR-2 Filing Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a public-safe ITR-2 filing skill and NRI extension that guide a user from tailored document collection through portal, preview, and acknowledgement review.

**Architecture:** Keep the common journey in `filing-itr2` and place only foreign-residence decisions in `filing-itr2-nri`. Keep each `SKILL.md` concise and load detailed checklists and portal guards from one-level reference files.

**Tech Stack:** Markdown Agent Skills, YAML interface metadata, Python standard-library contract tests, Git.

## Global Constraints

- Ask one focused question or request one action at a time.
- Infer facts from documents before asking.
- Use only official current-year sources for mutable tax rules.
- Never copy real taxpayer data into the repository.
- Stop before payment, submission, OTP, or e-verification.
- Keep ITR-3 business/profession cases out of scope.

---

### Task 1: Contract tests and baseline

**Files:**
- Create: `tests/test_skill_contract.py`

**Interfaces:**
- Consumes: approved design in `docs/design.md`.
- Produces: executable checks for the two skill folders and their required behavior.

- [x] Write tests that require simple interaction, tailored collection, capital-gain guards, portal screenshot looping, preview audit, acknowledgement audit, and NRI facts.
- [x] Run `python3 -m unittest -v tests/test_skill_contract.py`.
- [x] Verify RED: tests fail because the skill folders do not exist.

### Task 2: Base ITR-2 skill

**Files:**
- Create: `filing-itr2/SKILL.md`
- Create: `filing-itr2/agents/openai.yaml`
- Create: `filing-itr2/references/intake-and-reconciliation.md`
- Create: `filing-itr2/references/capital-gains-and-exemptions.md`
- Create: `filing-itr2/references/portal-journey.md`
- Create: `filing-itr2/references/preview-and-ack-review.md`

**Interfaces:**
- Consumes: user facts and source documents.
- Produces: a reconciled filing ledger, schedule map, one-step portal guidance, and final review results.

- [x] Initialize `filing-itr2` using the official skill scaffold generator.
- [x] Implement the minimal journey required by the contract tests.
- [x] Run the contract tests and skill validator.
- [x] Verify GREEN for all base-skill assertions.

### Task 3: NRI extension

**Files:**
- Create: `filing-itr2-nri/SKILL.md`
- Create: `filing-itr2-nri/agents/openai.yaml`
- Create: `filing-itr2-nri/references/nri-residency-and-treaty.md`
- Create: `filing-itr2-nri/references/nri-portal-checks.md`

**Interfaces:**
- Consumes: the base `filing-itr2` journey plus foreign-residence facts.
- Produces: residency basis, NRI evidence checklist, treaty readiness, and NRI-specific portal guidance.

- [x] Verify the NRI contract tests still fail before creating the extension.
- [x] Initialize the extension using the official skill scaffold generator.
- [x] Implement only NRI-specific additions and require the base skill.
- [x] Run the contract tests and both skill validators.
- [x] Verify GREEN for all NRI assertions.

### Task 4: Scenario and privacy review

**Files:**
- Create: `tests/test_scenarios.py`

**Interfaces:**
- Consumes: the completed skill text.
- Produces: regression checks for common failure modes without taxpayer data.

- [x] Add anonymized tests for debt-fund misclassification, Section 54F chronology, missing broker reports, missing residency days, preview mismatch, and acknowledgement status.
- [x] Run all tests and inspect every failure.
- [x] Search the repository for likely personal identifiers and raw attachments.
- [x] Correct gaps without broadening the user questionnaire.

### Task 5: Multi-round verification and Git handoff

**Files:**
- Modify only files implicated by review findings.

**Interfaces:**
- Consumes: all skill and test files.
- Produces: a validated, commit-ready Git worktree.

- [x] Review 1: requirement-by-requirement coverage against `docs/design.md`.
- [x] Review 2: simplicity and progressive-disclosure review.
- [x] Review 3: tax-safety, privacy, and escalation review.
- [x] Run `python3 -m unittest discover -s tests -v`.
- [x] Run `quick_validate.py` for both skills.
- [x] Inspect `git diff --check`, `git status --short`, and the final file tree.
