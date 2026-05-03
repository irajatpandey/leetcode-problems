import unittest


# Problem: Sum of Beauty of All Substrings
# The beauty of a string is the difference between the highest frequency and
# lowest frequency of characters present in it.
#
# Given a string s, return the sum of beauty of all of its substrings.
#
# Examples:
# Input: s = "aabcb"
# Output: 5
#
# Input: s = "aabcbaa"
# Output: 17
#
# Constraints:
# - s consists of lowercase English letters.


class Solution:
    def beauty_sum(self, s: str) -> int:
        # TODO: Implement this.
        pass


class TestSumOfBeautyOfAllSubstrings(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_example(self) -> None:
        self.assertEqual(self.solution.beauty_sum("aabcb"), 5)

    def test_second_example(self) -> None:
        self.assertEqual(self.solution.beauty_sum("aabcbaa"), 17)

    def test_single_character(self) -> None:
        self.assertEqual(self.solution.beauty_sum("a"), 0)


if __name__ == "__main__":
    unittest.main()
