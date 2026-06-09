"""
Problem: Valid Anagram (https://leetcode.com/problems/valid-anagram/)

Description:
    Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
    i.e., both strings contain the same characters with the same frequencies.

Example:
    Input: s = "anagram", t = "nagaram"
    Output: True

Approach:
    Count characters for both strings and compare the resulting maps.

Time Complexity: O(n) where n is the length of the strings
Space Complexity: O(k) where k is the number of distinct characters
"""

from typing import Dict


class Solution:
    """Solution for the Valid Anagram problem.

    The `isAnagram` method counts characters in both strings and compares the
    count dictionaries.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """Return True if `t` is an anagram of `s`.

        Args:
            s (str): First input string.
            t (str): Second input string to compare with `s`.

        Returns:
            bool: True if `t` is an anagram of `s`, False otherwise.
        """
        if len(s) != len(t):
            return False

        countS: Dict[str, int] = {}
        countT: Dict[str, int] = {}

        for a, b in zip(s, t):
            countS[a] = 1 + countS.get(a, 0)
            countT[b] = 1 + countT.get(b, 0)

        return countS == countT


# Alternative concise solution using collections.Counter:
# from collections import Counter
# def isAnagram(self, s: str, t: str) -> bool:
#     return Counter(s) == Counter(t)


def test_is_anagram():
    """Basic test cases for the Valid Anagram solution."""
    sol = Solution()

    # Example cases
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False

    # Edge cases
    assert sol.isAnagram("", "") is True
    assert sol.isAnagram("a", "a") is True
    assert sol.isAnagram("ab", "ba") is True
    assert sol.isAnagram("aabb", "abab") is True
    assert sol.isAnagram("aabb", "ab") is False

    # Unicode and repeated characters
    assert sol.isAnagram("àáç", "çáà") is True

    # Large input
    s = "a" * 1000 + "b" * 500
    t = "b" * 500 + "a" * 1000
    assert sol.isAnagram(s, t) is True

    print("All Valid-Anagram tests passed!")


if __name__ == "__main__":
    test_is_anagram()