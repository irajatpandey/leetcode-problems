import unittest


# Problem: Roman to Integer
# Given a roman numeral, convert it to an integer.
#
# Examples:
# Input: s = "III"
# Output: 3
#
# Input: s = "MCMXCIV"
# Output: 1994
#
# Constraints:
# - s is a valid roman numeral in the range [1, 3999].
# - Roman numerals use I, V, X, L, C, D, and M.


class Solution:
    def roman_to_int(self, s: str) -> int:
        # TODO: Implement this.
        pass


class TestRomanToInteger(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_simple_value(self) -> None:
        self.assertEqual(self.solution.roman_to_int("III"), 3)

    def test_subtractive_value(self) -> None:
        self.assertEqual(self.solution.roman_to_int("LVIII"), 58)

    def test_complex_value(self) -> None:
        self.assertEqual(self.solution.roman_to_int("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
