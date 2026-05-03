import unittest


# Problem: Sort Characters by Frequency
# Given a string s, sort it in decreasing order based on the frequency of the
# characters. Return the sorted string.
#
# Examples:
# Input: s = "tree"
# Output: "eert" or "eetr"
#
# Input: s = "cccaaa"
# Output: "cccaaa" or "aaaccc"
#
# Constraints:
# - s may contain uppercase letters, lowercase letters, digits, or symbols.
# - Multiple valid answers may exist when characters have the same frequency.


class Solution:
    def frequency_sort(self, s: str) -> str:
        # TODO: Implement this.
        pass


class TestSortCharactersByFrequency(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertFrequencySorted(self, result: str, expected_chars: str) -> None:
        self.assertEqual(sorted(result), sorted(expected_chars))
        frequencies = []
        i = 0
        while i < len(result):
            j = i
            while j < len(result) and result[j] == result[i]:
                j += 1
            frequencies.append(j - i)
            i = j
        self.assertEqual(frequencies, sorted(frequencies, reverse=True))

    def test_repeated_character(self) -> None:
        self.assertFrequencySorted(self.solution.frequency_sort("tree"), "tree")

    def test_tied_frequencies(self) -> None:
        self.assertFrequencySorted(self.solution.frequency_sort("cccaaa"), "cccaaa")

    def test_mixed_characters(self) -> None:
        self.assertFrequencySorted(self.solution.frequency_sort("Aabb"), "Aabb")


if __name__ == "__main__":
    unittest.main()
