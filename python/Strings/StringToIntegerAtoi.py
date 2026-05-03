import unittest


# Problem: String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a
# 32-bit signed integer.
#
# The function should ignore leading whitespace, handle an optional sign,
# read digits until the next non-digit character, and clamp the result to the
# 32-bit signed integer range.
#
# Examples:
# Input: s = "42"
# Output: 42
#
# Input: s = "   -42"
# Output: -42
#
# Constraints:
# - Return 0 if no valid conversion can be performed.
# - Clamp values below -2^31 or above 2^31 - 1.


class Solution:
    def my_atoi(self, s: str) -> int:
        # TODO: Implement this.
        pass


class TestStringToIntegerAtoi(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_positive_number(self) -> None:
        self.assertEqual(self.solution.my_atoi("42"), 42)

    def test_negative_with_spaces(self) -> None:
        self.assertEqual(self.solution.my_atoi("   -42"), -42)

    def test_stops_at_non_digit(self) -> None:
        self.assertEqual(self.solution.my_atoi("4193 with words"), 4193)

    def test_invalid_start(self) -> None:
        self.assertEqual(self.solution.my_atoi("words and 987"), 0)

    def test_clamps_underflow(self) -> None:
        self.assertEqual(self.solution.my_atoi("-91283472332"), -2147483648)


if __name__ == "__main__":
    unittest.main()
