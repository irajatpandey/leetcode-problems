import unittest


# Problem: Palindrome Check
# Given a string s, return True if it is a palindrome after converting all
# uppercase letters to lowercase and removing all non-alphanumeric characters.
#
# Examples:
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
#
# Input: s = "race a car"
# Output: False
#
# Constraints:
# - s may contain letters, digits, spaces, and symbols.


class Solution:
    def is_palindrome(self, s: str) -> bool:
        
        return True


class TestPalindromeCheck(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_valid_palindrome(self) -> None:
        self.assertTrue(self.solution.is_palindrome("A man, a plan, a canal: Panama"))

    def test_invalid_palindrome(self) -> None:
        self.assertFalse(self.solution.is_palindrome("race a car"))

    def test_empty_after_filtering(self) -> None:
        self.assertTrue(self.solution.is_palindrome(" "))


if __name__ == "__main__":
    unittest.main()
