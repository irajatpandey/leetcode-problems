import unittest
from typing import List


# Problem: Left Rotate Array by K Places
# Given an array of integers, rotate the array to the left by k positions
# and return the rotated array.
#
# Examples:
# Input: nums = [1, 2, 3, 4, 5], k = 2
# Output: [3, 4, 5, 1, 2]
#
# Input: nums = [1, 2, 3], k = 4
# Output: [2, 3, 1]
#
# Constraints:
# - The array may be empty.
# - k may be greater than the array length.


class Solution:
    def left_rotate_by_k(self, nums: List[int], k: int) -> List[int]:
        # TODO: Implement this.
        pass


class TestLeftRotateArrayByKPlaces(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_rotate_by_two(self) -> None:
        self.assertEqual(self.solution.left_rotate_by_k([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])

    def test_k_greater_than_length(self) -> None:
        self.assertEqual(self.solution.left_rotate_by_k([1, 2, 3], 4), [2, 3, 1])

    def test_zero_rotation(self) -> None:
        self.assertEqual(self.solution.left_rotate_by_k([1, 2, 3], 0), [1, 2, 3])

    def test_empty_array(self) -> None:
        self.assertEqual(self.solution.left_rotate_by_k([], 3), [])


if __name__ == "__main__":
    unittest.main()
