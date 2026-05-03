import unittest


# Problem: Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
#
# Examples:
# Input: s = "babad"
# Output: "bab" or "aba"
#
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
# - s may be empty.
# - If multiple answers exist, returning any one longest palindrome is valid.


class Solution:
    def longest_palindrome(self, s: str) -> str:
        # TODO: Implement this.
        pass


class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_odd_length_palindrome(self) -> None:
        self.assertIn(self.solution.longest_palindrome("babad"), ["bab", "aba"])

    def test_even_length_palindrome(self) -> None:
        self.assertEqual(self.solution.longest_palindrome("cbbd"), "bb")

    def test_single_character(self) -> None:
        self.assertEqual(self.solution.longest_palindrome("a"), "a")

    def test_empty_string(self) -> None:
        self.assertEqual(self.solution.longest_palindrome(""), "")


if __name__ == "__main__":
    unittest.main()
