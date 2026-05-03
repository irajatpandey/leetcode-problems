import unittest
from typing import List


# Problem: Maximum Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1s in
# the array.
#
# Examples:
# Input: nums = [1, 1, 0, 1, 1, 1]
# Output: 3
#
# Input: nums = [1, 0, 1, 1, 0, 1]
# Output: 2
#
# Constraints:
# - The array may be empty.
# - Elements are either 0 or 1.


class Solution:
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        # TODO: Implement this.
        maxSoFar = 0
        current_max = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 1: 
                current_max += 1
                maxSoFar = max(current_max, maxSoFar)
            else:
                current_max = 0

        return maxSoFar


class TestMaximumConsecutiveOnes(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_one(self) -> None:
        self.assertEqual(self.solution.find_max_consecutive_ones([1, 1, 0, 1, 1, 1]), 3)

    def test_example_two(self) -> None:
        self.assertEqual(self.solution.find_max_consecutive_ones([1, 0, 1, 1, 0, 1]), 2)

    def test_no_ones(self) -> None:
        self.assertEqual(self.solution.find_max_consecutive_ones([0, 0, 0]), 0)

    def test_empty_array(self) -> None:
        self.assertEqual(self.solution.find_max_consecutive_ones([]), 0)


if __name__ == "__main__":
    unittest.main()
