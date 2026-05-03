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
        m = len(nums1)
        n = len(nums2)
        merged = []

        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                value = nums1[i]
                i += 1
            else:
                value = nums2[j]
                j += 1

            if not merged or merged[-1] != value:
                merged.append(value)

        while i < m:
            if not merged or merged[-1] != nums1[i]:
                merged.append(nums1[i])
            i += 1

        while j < n:
            if not merged or merged[-1] != nums2[j]:
                merged.append(nums2[j])
            j += 1

        return merged



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
