import unittest


# Problem: Largest Odd Number in a String
# Given a string num representing a large integer, return the largest-valued
# odd integer that is a non-empty prefix of num. Return an empty string if no
# odd integer exists.
#
# Examples:
# Input: num = "52"
# Output: "5"
#
# Input: num = "4206"
# Output: ""
#
# Constraints:
# - num consists only of digits.
# - num does not contain leading zeroes unless num is "0".


class Solution:
    def largest_odd_number(self, num: str) -> str:
        # TODO: Implement this.
        pass


class TestLargestOddNumberInString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_prefix_is_answer(self) -> None:
        self.assertEqual(self.solution.largest_odd_number("52"), "5")

    def test_no_odd_number(self) -> None:
        self.assertEqual(self.solution.largest_odd_number("4206"), "")

    def test_whole_number_is_odd(self) -> None:
        self.assertEqual(self.solution.largest_odd_number("35427"), "35427")


if __name__ == "__main__":
    unittest.main()
