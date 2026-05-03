import unittest


# Problem: Check if Two Strings are Anagrams
# Given two strings s and t, return True if t is an anagram of s, and False
# otherwise.
#
# An anagram is a word or phrase formed by rearranging the letters of another.
#
# Examples:
# Input: s = "anagram", t = "nagaram"
# Output: True
#
# Input: s = "rat", t = "car"
# Output: False
#
# Constraints:
# - s and t consist of lowercase English letters.


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        # TODO: Implement this.
        pass


class TestValidAnagram(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_valid_anagram(self) -> None:
        self.assertTrue(self.solution.is_anagram("anagram", "nagaram"))

    def test_invalid_anagram(self) -> None:
        self.assertFalse(self.solution.is_anagram("rat", "car"))

    def test_different_lengths(self) -> None:
        self.assertFalse(self.solution.is_anagram("a", "ab"))


if __name__ == "__main__":
    unittest.main()
