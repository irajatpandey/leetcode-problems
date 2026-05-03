import unittest
from typing import List


# Problem: Move Zeros to End
# Given an integer array nums, move all 0s to the end while maintaining the
# relative order of the non-zero elements.
#
# Examples:
# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Input: nums = [0]
# Output: [0]
#
# Constraints:
# - The array may be empty.
# - Modify the array in-place and return it.


class Solution:
    def move_zeroes(self, nums: List[int]) -> List[int]:
        # TODO: Implement this.
        pass


class TestMoveZerosToEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_mixed_values(self) -> None:
        nums = [0, 1, 0, 3, 12]
        self.assertEqual(self.solution.move_zeroes(nums), [1, 3, 12, 0, 0])

    def test_single_zero(self) -> None:
        nums = [0]
        self.assertEqual(self.solution.move_zeroes(nums), [0])

    def test_no_zeroes(self) -> None:
        nums = [1, 2, 3]
        self.assertEqual(self.solution.move_zeroes(nums), [1, 2, 3])

    def test_empty_array(self) -> None:
        nums = []
        self.assertEqual(self.solution.move_zeroes(nums), [])


if __name__ == "__main__":
    unittest.main()
