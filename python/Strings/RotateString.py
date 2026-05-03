import unittest


# Problem: Rotate String
# Given two strings s and goal, return True if and only if s can become goal
# after some number of shifts on s.
#
# A shift moves the leftmost character of s to the rightmost position.
#
# Examples:
# Input: s = "abcde", goal = "cdeab"
# Output: True
#
# Input: s = "abcde", goal = "abced"
# Output: False
#
# Constraints:
# - s and goal may be empty.


class Solution:
    def rotate_string(self, s: str, goal: str) -> bool:
        # TODO: Implement this.
        pass


class TestRotateString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_can_rotate(self) -> None:
        self.assertTrue(self.solution.rotate_string("abcde", "cdeab"))

    def test_cannot_rotate(self) -> None:
        self.assertFalse(self.solution.rotate_string("abcde", "abced"))

    def test_empty_strings(self) -> None:
        self.assertTrue(self.solution.rotate_string("", ""))


if __name__ == "__main__":
    unittest.main()
