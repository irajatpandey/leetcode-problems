import unittest
from typing import List


# Problem: Linear Search
# Given an array of integers and a target value, return the index of the
# first occurrence of the target in the array.
#
# If the target is not present, return -1.
#
# Examples:
# Input: nums = [4, 2, 7, 1, 9], target = 7
# Output: 2
#
# Input: nums = [4, 2, 7, 1, 9], target = 3
# Output: -1
#
# Constraints:
# - The array may be empty.
# - If the target appears multiple times, return its first index.


class Solution:
    def linear_search(self, nums: List[int], target: int) -> int:
        # TODO: Implement this.
        pass


class TestLinearSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_target_found(self) -> None:
        self.assertEqual(self.solution.linear_search([4, 2, 7, 1, 9], 7), 2)

    def test_target_not_found(self) -> None:
        self.assertEqual(self.solution.linear_search([4, 2, 7, 1, 9], 3), -1)

    def test_first_element(self) -> None:
        self.assertEqual(self.solution.linear_search([10, 20, 30], 10), 0)

    def test_duplicate_target_returns_first_index(self) -> None:
        self.assertEqual(self.solution.linear_search([5, 1, 5, 2], 5), 0)


if __name__ == "__main__":
    unittest.main()
