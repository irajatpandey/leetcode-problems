import unittest
from typing import List


# Problem: Remove Duplicates from Sorted Array
# Given a sorted array nums, remove duplicate values in-place so each unique
# element appears only once. Return the number of unique elements.
#
# Examples:
# Input: nums = [1, 1, 2]
# Output: 2, nums starts with [1, 2]
#
# Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, nums starts with [0, 1, 2, 3, 4]
#
# Constraints:
# - The array may be empty.
# - The array is sorted in non-decreasing order.


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        # TODO: Implement this.
        pass


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_small_array(self) -> None:
        nums = [1, 1, 2]
        k = self.solution.remove_duplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_larger_array(self) -> None:
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.solution.remove_duplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])

    def test_empty_array(self) -> None:
        nums = []
        self.assertEqual(self.solution.remove_duplicates(nums), 0)


if __name__ == "__main__":
    unittest.main()
