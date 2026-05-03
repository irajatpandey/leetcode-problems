import unittest
from typing import List


# Problem: Check if the Array is Sorted II
# Given an array nums, return True if the array was originally sorted in
# non-decreasing order and then rotated some number of positions.
# Otherwise, return False.
#
# A sorted array may be rotated zero times, so an already sorted array is valid.
#
# Examples:
# Input: nums = [3, 4, 5, 1, 2]
# Output: True
#
# Input: nums = [2, 1, 3, 4]
# Output: False
#
# Input: nums = [1, 2, 3, 4, 5]
# Output: True
#
# Constraints:
# - The array will contain at least one element.
# - Duplicate values may be present.


class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
                if drops > 1:
                    return False

        return True


class TestCheckIfArrayIsSortedII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_sorted_and_rotated(self) -> None:
        self.assertTrue(self.solution.check([3, 4, 5, 1, 2]))

    def test_sorted_without_rotation(self) -> None:
        self.assertTrue(self.solution.check([1, 2, 3, 4, 5]))

    def test_not_sorted_and_rotated(self) -> None:
        self.assertFalse(self.solution.check([2, 1, 3, 4]))

    def test_all_equal(self) -> None:
        self.assertTrue(self.solution.check([1, 1, 1]))

    def test_with_duplicates(self) -> None:
        self.assertTrue(self.solution.check([2, 2, 3, 1, 2]))


if __name__ == "__main__":
    unittest.main()
