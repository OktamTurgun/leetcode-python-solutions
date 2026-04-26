class Solution:
    """Solution for Binary Search problem."""
    
    def search(self, nums: list[int], target: int) -> int:
        """
        Search for a target value in a sorted array using binary search.
        
        Args:
            nums: A sorted list of integers
            target: The value to search for
            
        Returns:
            The index of the target if found, otherwise -1
            
        Time Complexity: O(log n)
        Space Complexity: O(1)
            
        Examples:
            >>> sol = Solution()
            >>> sol.search([1, 3, 5, 7, 9], 5)
            2
            >>> sol.search([1, 3, 5, 7, 9], 4)
            -1
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":
    # Test cases
    sol = Solution()
    
    # Test case 1: Target found in the middle
    result1 = sol.search([1, 3, 5, 7, 9], 5)
    assert result1 == 2
    print("Test 1 passed: search([1, 3, 5, 7, 9], 5) = ", result1)
    
    # Test case 2: Target not found
    result2 = sol.search([1, 3, 5, 7, 9], 4)
    assert result2 == -1
    print("Test 2 passed: search([1, 3, 5, 7, 9], 4) = ", result2)
    
    # Test case 3: Target at the beginning
    result3 = sol.search([1, 3, 5, 7, 9], 1)
    assert result3 == 0
    print("Test 3 passed: search([1, 3, 5, 7, 9], 1) = ", result3)
    
    # Test case 4: Target at the end
    result4 = sol.search([1, 3, 5, 7, 9], 9)
    assert result4 == 4
    print("Test 4 passed: search([1, 3, 5, 7, 9], 9) = ", result4)
    
    # Test case 5: Single element array (found)
    result5 = sol.search([5], 5)
    assert result5 == 0
    print("Test 5 passed: search([5], 5) = ", result5)
    
    # Test case 6: Single element array (not found)
    result6 = sol.search([5], 3)
    assert result6 == -1
    print("Test 6 passed: search([5], 3) = ", result6)
    
    print("\nAll tests passed!")