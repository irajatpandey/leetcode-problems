import unittest
from typing import List


# Problem: Find Missing Number
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
#
# Examples:
# Input: nums = [3, 0, 1]
# Output: 2
#
# Input: nums = [0, 1]
# Output: 2
#
# Constraints:
# - Exactly one number is missing.
# - The numbers are distinct.


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        # TODO: Implement this.
        pass


class TestFindMissingNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_middle_missing(self) -> None:
        self.assertEqual(self.solution.missing_number([3, 0, 1]), 2)

    def test_last_missing(self) -> None:
        self.assertEqual(self.solution.missing_number([0, 1]), 2)

    def test_first_missing(self) -> None:
        self.assertEqual(self.solution.missing_number([1, 2]), 0)


if __name__ == "__main__":
    unittest.main()
