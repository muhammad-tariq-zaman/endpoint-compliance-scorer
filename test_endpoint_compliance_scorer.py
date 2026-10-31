import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import score, grade


def row(patched="yes", av="yes", enc="yes", fw="yes", seen="1"):
    return {"endpoint": "pc1", "os_patched": patched, "antivirus": av,
            "encrypted": enc, "firewall": fw, "last_seen_days": seen}


class TestComplianceScorer(unittest.TestCase):
    def test_full_score(self):
        self.assertEqual(score(row()), 100)

    def test_stale_loses_recency_points(self):
        self.assertEqual(score(row(seen="30")), 90)

    def test_missing_antivirus(self):
        self.assertEqual(score(row(av="no")), 75)

    def test_grades(self):
        self.assertEqual(grade(100), "COMPLIANT")
        self.assertEqual(grade(75), "AT RISK")
        self.assertEqual(grade(40), "NON-COMPLIANT")
