import unittest
from typing import List


# Problem: Largest Element
# Given an array of integers, return the largest element in the array.
#
# Examples:
# Input: nums = [1, 8, 7, 56, 90]
# Output: 90
#
# Input: nums = [-10, -3, -45, -1]
# Output: -1
#
# Constraints:
# - The array will contain at least one element.
# - Elements can be positive, negative, or zero.


class Solution:
    def largest_element(self, nums: List[int]) -> int:
        # TODO: Implement this.
        larget_element = float('-inf')
        for ele in nums:
            if ele > larget_element:
                larget_element = ele
        return larget_element
    


class TestLargestElement(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_positive_numbers(self) -> None:
        self.assertEqual(self.solution.largest_element([1, 8, 7, 56, 90]), 90)

    def test_negative_numbers(self) -> None:
        self.assertEqual(self.solution.largest_element([-10, -3, -45, -1]), -1)

    def test_single_element(self) -> None:
        self.assertEqual(self.solution.largest_element([42]), 42)

    def test_duplicate_largest(self) -> None:
        self.assertEqual(self.solution.largest_element([5, 9, 9, 2]), 9)


if __name__ == "__main__":
    unittest.main()
