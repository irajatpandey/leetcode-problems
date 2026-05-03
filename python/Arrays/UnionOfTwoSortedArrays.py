import unittest
from typing import List


# Problem: Union of Two Sorted Arrays
# Given two sorted arrays, return a sorted array containing the union of
# their unique elements.
#
# Examples:
# Input: nums1 = [1, 2, 2, 3], nums2 = [2, 3, 4]
# Output: [1, 2, 3, 4]
#
# Input: nums1 = [1, 1], nums2 = [1, 2]
# Output: [1, 2]
#
# Constraints:
# - Either array may be empty.
# - Both arrays are sorted in non-decreasing order.


class Solution:
    def find_union(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TODO: Implement this.

    
        pass


class TestUnionOfTwoSortedArrays(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_overlapping_arrays(self) -> None:
        self.assertEqual(self.solution.find_union([1, 2, 2, 3], [2, 3, 4]), [1, 2, 3, 4])

    def test_duplicate_values(self) -> None:
        self.assertEqual(self.solution.find_union([1, 1], [1, 2]), [1, 2])

    def test_first_array_empty(self) -> None:
        self.assertEqual(self.solution.find_union([], [1, 2]), [1, 2])

    def test_second_array_empty(self) -> None:
        self.assertEqual(self.solution.find_union([1, 2], []), [1, 2])


if __name__ == "__main__":
    unittest.main()
