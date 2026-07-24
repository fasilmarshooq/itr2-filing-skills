# ITR-2 Filing Skills

Guided Codex skills for compliant Indian ITR-2 filing. They help collect and
reconcile evidence, identify lawful tax-saving opportunities, guide portal
entry one screen at a time, and review the preview and acknowledgement.

| Skill | Purpose |
|---|---|
| `filing-itr2` | Common ITR-2 preparation, computation, portal, and verification journey |
| `filing-itr2-nri` | NRI/RNOR residency, foreign-jurisdiction, TRC, DTAA, and portal checks |

The NRI skill extends the base skill; install both for an NRI filing.

## Install

Install both skills from this public repository:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo fasilmarshooq/itr2-filing-skills \
  --path filing-itr2 filing-itr2-nri
```

They are installed under:

```text
~/.codex/skills/filing-itr2
~/.codex/skills/filing-itr2-nri
```

The skills are available from your next Codex turn.

### Install only the base skill

For an ITR-2 filing without the NRI extension:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo fasilmarshooq/itr2-filing-skills \
  --path filing-itr2
```

## Use

Start a new Codex task with:

```text
Use $filing-itr2 to guide me through my Indian ITR-2 filing one step at a time.
```

For an NRI filing:

```text
Use $filing-itr2-nri with $filing-itr2 to guide my NRI ITR-2 filing one step at a time.
```

The skills ask one focused question or request one screenshot/document at a
time. Do not provide passwords, OTPs, or portal credentials.

## Update

The installer does not overwrite an existing skill directory. Move or remove
the existing `~/.codex/skills/filing-itr2` and
`~/.codex/skills/filing-itr2-nri` directories, then run the installation
command again.

## Uninstall

Remove these directories from your Codex skills folder:

```text
~/.codex/skills/filing-itr2
~/.codex/skills/filing-itr2-nri
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
