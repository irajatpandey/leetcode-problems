import unittest


# Problem: Reverse Every Word in a String
# Given a string s, reverse the characters of each word while preserving
# whitespace and the original word order.
#
# Examples:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Input: s = "God Ding"
# Output: "doG gniD"
#
# Constraints:
# - s may contain one or more words separated by single spaces.


class Solution:
    def reverse_words_characters(self, s: str) -> str:
        # TODO: Implement this.
        pass


class TestReverseEveryWordInString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_sentence(self) -> None:
        self.assertEqual(
            self.solution.reverse_words_characters("Let's take LeetCode contest"),
            "s'teL ekat edoCteeL tsetnoc",
        )

    def test_two_words(self) -> None:
        self.assertEqual(self.solution.reverse_words_characters("God Ding"), "doG gniD")

    def test_single_word(self) -> None:
        self.assertEqual(self.solution.reverse_words_characters("hello"), "olleh")


if __name__ == "__main__":
    unittest.main()
