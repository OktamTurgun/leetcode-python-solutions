"""
Problem: Two Sum (https://leetcode.com/problems/two-sum/)

Description:
    Given an array of integers nums and an integer target, 
    return the indices of the two numbers that add up to the target.
    You can assume that each input has exactly one solution, 
    and you cannot use the same element twice.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1]

Approach:
    Using a Hash Map (Dictionary) to store values we've seen before.
    As we iterate through the array, we check if the complement 
    (target - current number) exists in our hash map.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash map stores up to n elements
"""


class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        """
        Find indices of two numbers that add up to target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices where nums[i] + nums[j] == target
        """
        prev_map = {}  # Dictionary to store num -> index
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[num] = i
        
        return [] 


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    # Test 1: Basic case
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test 2: Different numbers
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test 3: Negative numbers
    assert solution.twoSum([-1, -2, -3, 5, 6], 1) == [3, 4]
    
    print("All test cases passed!")