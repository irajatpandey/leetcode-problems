import unittest
from typing import List


class Solution:
    def left_rotate_by_one(self, nums: List[int]) -> List[int]:
        # TODO: Implement this.
        pass


class TestLeftRotateArrayByOne(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_multiple_elements(self) -> None:
        self.assertEqual(self.solution.left_rotate_by_one([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_two_elements(self) -> None:
        self.assertEqual(self.solution.left_rotate_by_one([10, 20]), [20, 10])

    def test_single_element(self) -> None:
        self.assertEqual(self.solution.left_rotate_by_one([7]), [7])

    def test_empty_array(self) -> None:
        self.assertEqual(self.solution.left_rotate_by_one([]), [])


if __name__ == "__main__":
    unittest.main()
