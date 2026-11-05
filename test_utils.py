import unittest
from utils import format_pace


class TestFormatPace(unittest.TestCase):
    def test_quarter_minute(self):
        self.assertEqual(format_pace(5.25), "5:15 min/km")

    def test_whole_minute(self):
        self.assertEqual(format_pace(6.0), "6:00 min/km")

    def test_leading_zero(self):
        self.assertEqual(format_pace(5 + 5 / 60), "5:05 min/km")

    def test_rounding_to_next_minute(self):
        self.assertEqual(format_pace(5.999), "6:00 min/km")


if __name__ == "__main__":
    unittest.main()