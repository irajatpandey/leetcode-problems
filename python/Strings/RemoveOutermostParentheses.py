import unittest


# Problem: Remove Outermost Parentheses
# Given a valid parentheses string s, remove the outermost parentheses of
# every primitive substring in the primitive decomposition of s.
#
# Examples:
# Input: s = "(()())(())"
# Output: "()()()"
#
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
#
# Constraints:
# - s is a valid parentheses string.
# - s consists only of '(' and ')'.


class Solution:
    def remove_outer_parentheses(self, s: str) -> str:
        # TODO: Implement this.
        pass


class TestRemoveOutermostParentheses(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_multiple_primitives(self) -> None:
        self.assertEqual(self.solution.remove_outer_parentheses("(()())(())"), "()()()")

    def test_nested_primitives(self) -> None:
        self.assertEqual(self.solution.remove_outer_parentheses("(()())(())(()(()))"), "()()()()(())")

    def test_single_primitive(self) -> None:
        self.assertEqual(self.solution.remove_outer_parentheses("()()"), "")


if __name__ == "__main__":
    unittest.main()
