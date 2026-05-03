import unittest
from typing import List


# Problem: Two Sum
# Given an array of integers nums and an integer target, return the indices
# of the two numbers such that they add up to target.
#
# Each input has exactly one solution, and the same element cannot be used
# twice.
#
# Examples:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
#
# Constraints:
# - The array will contain at least two elements.
# - Exactly one valid pair exists.


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # TODO: Implement this.
        pass


class TestTwoSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_one(self) -> None:
        self.assertEqual(self.solution.two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example_two(self) -> None:
        self.assertEqual(self.solution.two_sum([3, 2, 4], 6), [1, 2])

    def test_duplicate_values(self) -> None:
        self.assertEqual(self.solution.two_sum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
