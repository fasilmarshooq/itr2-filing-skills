# ITR-2 Filing Skills

Reusable Agent Skills for compliant Indian ITR-2 filing. They help collect
and reconcile evidence, identify lawful tax-saving opportunities, guide portal
entry one screen at a time, and review the preview and acknowledgement.

The skills follow the open
[Agent Skills specification](https://agentskills.io/specification) and work
with OpenAI Codex, Claude Code, and Cursor.

| Skill | Purpose |
|---|---|
| `filing-itr2` | Common ITR-2 preparation, computation, portal, and verification journey |
| `filing-itr2-nri` | NRI/RNOR residency, foreign-jurisdiction, TRC, DTAA, and portal checks |

The NRI skill extends the base skill; install both for an NRI filing.

## Install

You need Node.js with `npx`. Install both skills globally for Codex, Claude
Code, and Cursor:

```bash
npx skills add fasilmarshooq/itr2-filing-skills \
  --skill filing-itr2 \
  --skill filing-itr2-nri \
  -g \
  -a codex \
  -a claude-code \
  -a cursor \
  --copy
```

The installer places each skill in the correct user-level directory for the
selected agents. Start a new agent session after installation if the skills do
not appear immediately.

### Install only the base skill

For an ITR-2 filing without the NRI extension:

```bash
npx skills add fasilmarshooq/itr2-filing-skills \
  --skill filing-itr2 \
  -g \
  -a codex \
  -a claude-code \
  -a cursor \
  --copy
```

## Use

In a new agent session, ask:

```text
Use the filing-itr2 skill to guide me through my Indian ITR-2 filing one step at a time.
```

For an NRI filing:

```text
Use filing-itr2-nri together with filing-itr2 to guide my NRI ITR-2 filing one step at a time.
```

The skills ask one focused question or request one screenshot/document at a
time. Do not provide passwords, OTPs, or portal credentials.

## Compatibility

The portable workflow is defined in each skill's `SKILL.md` and referenced
files. The optional `agents/openai.yaml` files provide display metadata for
OpenAI clients; they do not control the workflow and are ignored by agents
that do not use them.

## Update

Update both installed skills through the same cross-agent CLI:

```bash
npx skills update filing-itr2 filing-itr2-nri -g
```

## Uninstall

Remove both skills from their installed agent directories:

```bash
npx skills remove filing-itr2 filing-itr2-nri -g
```

## Verify the repository

```bash
python3 -m unittest discover -s tests -v
```

## Important

These skills provide guided filing assistance, not legal or professional tax
advice. Tax rules and portal fields change by assessment year, so the skills
require current official sources for mutable rules. Keep taxpayer documents
private and never commit them to this repository.

## License

[MIT](LICENSE)
