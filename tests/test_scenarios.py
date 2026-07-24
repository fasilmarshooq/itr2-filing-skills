from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "filing-itr2"
NRI = ROOT / "filing-itr2-nri"


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8").lower()


def public_files():
    for folder in (BASE, NRI):
        yield from folder.rglob("*")


def repository_files():
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        yield path


class FilingScenarios(unittest.TestCase):
    def test_debt_fund_is_not_mapped_to_unquoted_shares(self) -> None:
        gains = text(BASE / "references" / "capital-gains-and-exemptions.md")
        self.assertIn("debt/non-equity mutual fund", gains)
        self.assertIn("do not place mutual fund", gains)
        self.assertIn("assets other than unquoted shares", gains)

    def test_54f_requires_evidence_and_chronology(self) -> None:
        gains = text(BASE / "references" / "capital-gains-and-exemptions.md")
        normalized = " ".join(gains.split())
        for term in (
            "original long-term asset",
            "other than a residential house",
            "not available for short-term",
            "transfer date",
            "registration",
            "chronology",
            "net consideration",
            "capital gains accounts scheme",
            "do not substitute the new-house",
        ):
            self.assertIn(term, normalized)

    def test_tax_saving_choices_have_a_simple_shape(self) -> None:
        skill = text(BASE / "SKILL.md")
        self.assertIn("supported now", skill)
        self.assertIn("needs evidence", skill)
        self.assertIn("not eligible", skill)

    def test_preview_mismatch_and_ack_status_are_not_skipped(self) -> None:
        review = text(BASE / "references" / "preview-and-ack-review.md")
        for term in (
            "pdf value",
            "expected value",
            "source",
            "tax effect",
            "acknowledgement",
            "verification status",
            "refund",
        ):
            self.assertIn(term, review)

    def test_missing_residency_days_blocks_nri_conclusion(self) -> None:
        residency = text(
            NRI / "references" / "nri-residency-and-treaty.md"
        )
        self.assertIn("entry/exit calendar", residency)
        self.assertIn("current financial year", residency)
        self.assertIn("four preceding", residency)
        self.assertIn("within 180 days", residency)


class PublicSafety(unittest.TestCase):
    def test_no_raw_taxpayer_artifacts_are_committed(self) -> None:
        forbidden_suffixes = {
            ".png",
            ".jpg",
            ".jpeg",
            ".pdf",
            ".xlsx",
            ".xls",
            ".csv",
            ".json",
        }
        offenders = [
            str(path.relative_to(ROOT))
            for path in repository_files()
            if path.is_file() and path.suffix.lower() in forbidden_suffixes
        ]
        self.assertEqual([], offenders)

    def test_no_machine_paths_or_long_identifiers_in_skill_files(self) -> None:
        offenders = []
        for path in public_files():
            if not path.is_file():
                continue
            content = path.read_text(encoding="utf-8")
            if (
                "/Users/" in content
                or re.search(r"\b\d{12,}\b", content)
                or re.search(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b", content)
            ):
                offenders.append(str(path.relative_to(ROOT)))
        self.assertEqual([], offenders)

    def test_repository_is_legally_reusable(self) -> None:
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("MIT License", license_text)

    def test_main_skills_remain_compact(self) -> None:
        base_words = len((BASE / "SKILL.md").read_text().split())
        nri_words = len((NRI / "SKILL.md").read_text().split())
        self.assertLess(base_words, 500)
        self.assertLess(nri_words, 400)


if __name__ == "__main__":
    unittest.main()
