
"""
Problem: Majority Element (https://leetcode.com/problems/majority-element/)

Description:
    Given an array `nums` of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume the majority element always exists in the array.

Example:
    Input: nums = [3, 2, 3]
    Output: 3
    Explanation: 3 appears more than ⌊3 / 2⌋ = 1 time

Approach:
    Uses Boyer-Moore Majority Vote algorithm. Keep a candidate and a count.
    If count is 0, select a new candidate. For each element, increment count
    if it matches the candidate, otherwise decrement. The last candidate is
    guaranteed to be the majority element.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) - only using two variables
"""


class Solution:
    """Solution for the Majority Element problem.

    The `majorityElement` method uses the Boyer-Moore Majority Vote algorithm
    to find the element appearing more than n/2 times in O(1) space.
    """

    def majorityElement(self, nums: list[int]) -> int:
        """Return the majority element that appears more than n/2 times.

        Args:
            nums (list[int]): Array of integers.

        Returns:
            int: The majority element in the array.
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


# Alternative approach using hash map:
# def majorityElement(self, nums: list[int]) -> int:
#     count_map = {}
#     half = len(nums) // 2
#     for num in nums:
#         count_map[num] = 1 + count_map.get(num, 0)
#         if count_map[num] > half:
#             return num


def test_majority_element():
    """Test cases for the Majority Element solution."""
    sol = Solution()

    # Example cases
    assert sol.majorityElement([3, 2, 3]) == 3
    assert sol.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2

    # Edge cases
    assert sol.majorityElement([1]) == 1
    assert sol.majorityElement([1, 1]) == 1
    assert sol.majorityElement([1, 2, 1]) == 1

    # Large majority
    assert sol.majorityElement([1] * 100 + [2] * 50) == 1

    # Negative numbers
    assert sol.majorityElement([-1, -1, -1, 2, 2]) == -1

    print("All Majority-Element tests passed!")


if __name__ == "__main__":
    test_majority_element()