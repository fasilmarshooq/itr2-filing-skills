from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "filing-itr2"
NRI = ROOT / "filing-itr2-nri"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class BaseSkillContract(unittest.TestCase):
    def setUp(self) -> None:
        self.skill = read(BASE / "SKILL.md")

    def test_guides_one_step_at_a_time(self) -> None:
        self.assertIn("one focused question", self.skill.lower())
        self.assertIn("infer", self.skill.lower())
        self.assertIn("why", self.skill.lower())

    def test_collects_only_relevant_evidence_before_portal(self) -> None:
        intake = read(BASE / "references" / "intake-and-reconciliation.md").lower()
        for term in (
            "ais",
            "tis",
            "26as",
            "tax p&l",
            "health insurance",
            "tuition",
            "home-loan",
        ):
            self.assertIn(term, intake)
        self.assertIn("tailored", intake)

    def test_has_capital_gain_classification_and_54f_guards(self) -> None:
        gains = read(BASE / "references" / "capital-gains-and-exemptions.md").lower()
        for term in ("111a", "112a", "debt", "unquoted", "54f", "chronology"):
            self.assertIn(term, gains)
        self.assertIn("do not", gains)

    def test_covers_portal_preview_and_acknowledgement(self) -> None:
        portal = read(BASE / "references" / "portal-journey.md").lower()
        review = read(BASE / "references" / "preview-and-ack-review.md").lower()
        self.assertIn("screenshot", portal)
        self.assertIn("one action", portal)
        self.assertIn("preview pdf", review)
        self.assertIn("acknowledgement", review)
        self.assertIn("refund", review)

    def test_requires_current_official_rules_and_user_control(self) -> None:
        lower = self.skill.lower()
        self.assertIn("official", lower)
        self.assertIn("assessment year", lower)
        for term in ("password", "otp", "submit", "e-verification"):
            self.assertIn(term, lower)


class NriSkillContract(unittest.TestCase):
    def setUp(self) -> None:
        self.skill = read(NRI / "SKILL.md")
        self.residency = read(
            NRI / "references" / "nri-residency-and-treaty.md"
        ).lower()

    def test_extends_base_instead_of_repeating_it(self) -> None:
        self.assertIn("filing-itr2", self.skill)
        self.assertIn("required", self.skill.lower())

    def test_collects_residency_and_treaty_evidence(self) -> None:
        for term in (
            "current financial year",
            "four preceding",
            "tax jurisdiction",
            "taxpayer identification number",
            "trc",
            "fpi",
        ):
            self.assertIn(term, self.residency)

    def test_does_not_claim_treaty_relief_without_support(self) -> None:
        self.assertIn("do not claim", self.residency)
        self.assertIn("official", self.residency)
        self.assertIn("evidence", self.residency)


class ReadmeContract(unittest.TestCase):
    def test_readme_has_cross_agent_install_and_usage(self) -> None:
        readme = read(ROOT / "README.md")
        for term in (
            "npx skills add fasilmarshooq/itr2-filing-skills",
            "--skill filing-itr2",
            "--skill filing-itr2-nri",
            "-a codex",
            "-a claude-code",
            "-a cursor",
            "OpenAI Codex",
            "Claude Code",
            "Cursor",
            "new agent session",
            "Update",
            "Uninstall",
        ):
            self.assertIn(term, readme)

    def test_readme_is_not_tied_to_the_codex_installer(self) -> None:
        readme = read(ROOT / "README.md")
        self.assertNotIn("~/.codex/skills/.system/skill-installer", readme)
        self.assertNotIn("Guided Codex skills", readme)
        self.assertNotIn("next Codex turn", readme)


if __name__ == "__main__":
    unittest.main()
