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

        totals, skipped = summarize_runs(rows)
        self.assertEqual(skipped, 0)

        self.assertEqual(totals["Danial"]["runs"], 2)
        self.assertEqual(totals["Danial"]["distance"], 10.0)
        self.assertEqual(totals["Danial"]["duration"], 85.0)

        self.assertEqual(totals["Ali"]["runs"], 1)
        self.assertEqual(totals["Ali"]["distance"], 2.0)
        self.assertEqual(totals["Ali"]["duration"], 14.0)

        def test_empty_input(self):
            self.assertEqual(summarize_runs([]), ({}, 0))

    def test_skips_invalid_rows(self):
        rows = [
            {
                "runner": "Danial",
                "distance_km": "5",
                "duration_minutes": "30"
            },
            {
                "runner": "Ali",
                "distance_km": "hello",
                "duration_minutes": "14"
            },
            {
                "runner": "Danial",
                "distance_km": "0",
                "duration_minutes": "10"
            }
        ]

        totals, skipped = summarize_runs(rows)

        self.assertEqual(skipped, 2)
        self.assertEqual(len(totals), 1)
        self.assertEqual(totals["Danial"]["runs"], 1)
        self.assertEqual(totals["Danial"]["distance"], 5.0)
        self.assertEqual(totals["Danial"]["duration"], 30.0)
if __name__ == "__main__":
    unittest.main()