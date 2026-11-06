import unittest
from utils import summarize_runs


class TestSummary(unittest.TestCase):
    def test_groups_runs_by_runner(self):
        rows = [
            {
                "runner": "Danial",
                "distance_km": "5",
                "duration_minutes": "45"
            },
            {
                "runner": "Danial",
                "distance_km": "5",
                "duration_minutes": "40"
            },
            {
                "runner": "Ali",
                "distance_km": "2",
                "duration_minutes": "14"
            }
        ]

        totals = summarize_runs(rows)

        self.assertEqual(totals["Danial"]["runs"], 2)
        self.assertEqual(totals["Danial"]["distance"], 10.0)
        self.assertEqual(totals["Danial"]["duration"], 85.0)

        self.assertEqual(totals["Ali"]["runs"], 1)
        self.assertEqual(totals["Ali"]["distance"], 2.0)
        self.assertEqual(totals["Ali"]["duration"], 14.0)

    def test_empty_input(self):
        self.assertEqual(summarize_runs([]), {})


if __name__ == "__main__":
    unittest.main()