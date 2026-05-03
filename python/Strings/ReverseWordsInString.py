import unittest


# Problem: Reverse Words in a Given String
# Given a string s, reverse the order of the words.
#
# A word is a sequence of non-space characters. The returned string should
# contain words separated by a single space, with no leading or trailing spaces.
#
# Examples:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
# Input: s = "  hello world  "
# Output: "world hello"
#
# Constraints:
# - s may contain leading, trailing, or multiple spaces between words.


class Solution:
    def reverse_words(self, s: str) -> str:
        # TODO: Implement this.
        pass


class TestReverseWordsInString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_simple_sentence(self) -> None:
        self.assertEqual(self.solution.reverse_words("the sky is blue"), "blue is sky the")

    def test_leading_and_trailing_spaces(self) -> None:
        self.assertEqual(self.solution.reverse_words("  hello world  "), "world hello")

    def test_multiple_spaces_between_words(self) -> None:
        self.assertEqual(self.solution.reverse_words("a good   example"), "example good a")


if __name__ == "__main__":
    unittest.main()
