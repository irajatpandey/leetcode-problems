import unittest
from typing import List


class Solution:
    def linear_search(self, nums: List[int], target: int) -> int:
        # TODO: Implement this.
        result = -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1


class TestLinearSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_target_found(self) -> None:
        self.assertEqual(self.solution.linear_search([4, 2, 7, 1, 9], 7), 2)

    def test_target_not_found(self) -> None:
        self.assertEqual(self.solution.linear_search([4, 2, 7, 1, 9], 3), -1)

    def test_first_element(self) -> None:
        self.assertEqual(self.solution.linear_search([10, 20, 30], 10), 0)

    def test_duplicate_target_returns_first_index(self) -> None:
        self.assertEqual(self.solution.linear_search([5, 1, 5, 2], 5), 0)


if __name__ == "__main__":
    unittest.main()
