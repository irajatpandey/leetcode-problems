import unittest
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        # TODO: Implement this.
        pass


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
