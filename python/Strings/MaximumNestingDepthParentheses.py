import unittest


# Problem: Maximum Nesting Depth of the Parentheses
# Given a valid parentheses string s, return the maximum nesting depth of the
# parentheses.
#
# Examples:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
#
# Input: s = "(1)+((2))+(((3)))"
# Output: 3
#
# Constraints:
# - s is a valid parentheses string.
# - s may contain digits, operators, letters, spaces, and parentheses.


class Solution:
    def max_depth(self, s: str) -> int:
        # TODO: Implement this.
        pass


class TestMaximumNestingDepthParentheses(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_expression_depth(self) -> None:
        self.assertEqual(self.solution.max_depth("(1+(2*3)+((8)/4))+1"), 3)

    def test_nested_groups(self) -> None:
        self.assertEqual(self.solution.max_depth("(1)+((2))+(((3)))"), 3)

    def test_no_parentheses(self) -> None:
        self.assertEqual(self.solution.max_depth("1+2"), 0)


if __name__ == "__main__":
    unittest.main()
