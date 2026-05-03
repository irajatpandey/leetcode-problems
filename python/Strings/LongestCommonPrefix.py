import unittest
from typing import List


# Problem: Longest Common Prefix
# Given an array of strings strs, return the longest common prefix among them.
# If there is no common prefix, return an empty string.
#
# Examples:
# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"
#
# Input: strs = ["dog", "racecar", "car"]
# Output: ""
#
# Constraints:
# - strs may be empty.
# - Strings may be empty.


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        # TODO: Implement this.
        pass


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_common_prefix(self) -> None:
        self.assertEqual(self.solution.longest_common_prefix(["flower", "flow", "flight"]), "fl")

    def test_no_common_prefix(self) -> None:
        self.assertEqual(self.solution.longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_empty_list(self) -> None:
        self.assertEqual(self.solution.longest_common_prefix([]), "")

    def test_single_string(self) -> None:
        self.assertEqual(self.solution.longest_common_prefix(["alone"]), "alone")


if __name__ == "__main__":
    unittest.main()
