"""
Problem: Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)

Description:
    Given an integer array nums, return True if any value appears at least twice
    in the array, and return False if every element is distinct.

Example:
    Input: nums = [1, 2, 3, 1]
    Output: True

Approach:
    Use a set to record values seen while iterating through nums.
    If a number is already in the set, a duplicate exists and we return True.

Time Complexity: O(n) - one pass through nums
Space Complexity: O(n) - set may store all elements in the worst case
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Determine if the input list contains any duplicate integers.

        Args:
            nums: A list of integers.

        Returns:
            True if there are duplicate values, otherwise False.
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


def run_tests() -> None:
    """Run test cases for the Contains Duplicate solution."""
    solution = Solution()

    assert solution.containsDuplicate([1, 2, 3, 1]) is True
    assert solution.containsDuplicate([1, 2, 3, 4]) is False
    assert solution.containsDuplicate([]) is False
    assert solution.containsDuplicate([42]) is False
    assert solution.containsDuplicate([5, 5, 5, 5]) is True
    assert solution.containsDuplicate([-1, -2, -3, -1]) is True

    print("✅ All test cases passed!")


if __name__ == "__main__":
    run_tests()