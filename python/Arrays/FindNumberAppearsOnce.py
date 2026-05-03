import unittest
from typing import List


# Problem: Find the Number that Appears Once
# Given a non-empty array of integers nums, every element appears twice
# except for one. Return the element that appears once.
#
# Examples:
# Input: nums = [2, 2, 1]
# Output: 1
#
# Input: nums = [4, 1, 2, 1, 2]
# Output: 4
#
# Constraints:
# - Exactly one element appears once.
# - Every other element appears twice.


class Solution:
    def single_number(self, nums: List[int]) -> int:
        # TODO: Implement this.
            
        


class TestFindNumberAppearsOnce(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_short_array(self) -> None:
        self.assertEqual(self.solution.single_number([2, 2, 1]), 1)

    def test_larger_array(self) -> None:
        self.assertEqual(self.solution.single_number([4, 1, 2, 1, 2]), 4)

    def test_single_element(self) -> None:
        self.assertEqual(self.solution.single_number([7]), 7)


if __name__ == "__main__":
    unittest.main()
