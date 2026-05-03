import unittest


# Problem: Isomorphic String
# Given two strings s and t, return True if s and t are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t,
# with each character mapping to exactly one character and no two characters
# mapping to the same character.
#
# Examples:
# Input: s = "egg", t = "add"
# Output: True
#
# Input: s = "foo", t = "bar"
# Output: False
#
# Constraints:
# - s and t have the same length.
# - s and t may contain any valid characters.


class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        # TODO: Implement this.
        pass


class TestIsomorphicString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_isomorphic_strings(self) -> None:
        self.assertTrue(self.solution.is_isomorphic("egg", "add"))

    def test_not_isomorphic_strings(self) -> None:
        self.assertFalse(self.solution.is_isomorphic("foo", "bar"))

    def test_repeated_target_conflict(self) -> None:
        self.assertFalse(self.solution.is_isomorphic("badc", "baba"))


if __name__ == "__main__":
    unittest.main()
