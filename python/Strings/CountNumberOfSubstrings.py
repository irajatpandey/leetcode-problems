import unittest


# Problem: Count Number of Substrings
# Given a string s consisting only of characters 'a', 'b', and 'c', return the
# number of substrings containing at least one occurrence of all three
# characters.
#
# Examples:
# Input: s = "abcabc"
# Output: 10
#
# Input: s = "aaacb"
# Output: 3
#
# Constraints:
# - s consists only of 'a', 'b', and 'c'.


class Solution:
    def number_of_substrings(self, s: str) -> int:
        # TODO: Implement this.
        pass


class TestCountNumberOfSubstrings(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_repeating_pattern(self) -> None:
        self.assertEqual(self.solution.number_of_substrings("abcabc"), 10)

    def test_clustered_characters(self) -> None:
        self.assertEqual(self.solution.number_of_substrings("aaacb"), 3)

    def test_no_valid_substring(self) -> None:
        self.assertEqual(self.solution.number_of_substrings("aaaa"), 0)


if __name__ == "__main__":
    unittest.main()
