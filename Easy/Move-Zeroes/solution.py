class Solution:
    """Solution for Move Zeroes problem."""
    
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Move all zeroes in the array to the end while maintaining relative order of non-zero elements.
        
        This function modifies the array in-place.
        
        Args:
            nums: A list of integers
            
        Returns:
            None (modifies nums in-place)
            
        Time Complexity: O(n)
        Space Complexity: O(1)
            
        Examples:
            >>> sol = Solution()
            >>> nums = [0, 1, 0, 3, 12]
            >>> sol.moveZeroes(nums)
            >>> nums
            [1, 3, 12, 0, 0]
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


if __name__ == "__main__":
    # Test cases
    sol = Solution()
    
    # Test case 1: Basic case
    test1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(test1)
    assert test1 == [1, 3, 12, 0, 0]
    print("Test 1 passed: [0, 1, 0, 3, 12] -> ", test1)
    
    # Test case 2: No zeroes
    test2 = [1, 2, 3]
    sol.moveZeroes(test2)
    assert test2 == [1, 2, 3]
    print("Test 2 passed: [1, 2, 3] -> ", test2)
    
    # Test case 3: All zeroes
    test3 = [0, 0, 1]
    sol.moveZeroes(test3)
    assert test3 == [1, 0, 0]
    print("Test 3 passed: [0, 0, 1] -> ", test3)
    
    # Test case 4: Single element (zero)
    test4 = [0]
    sol.moveZeroes(test4)
    assert test4 == [0]
    print("Test 4 passed: [0] -> ", test4)
    
    # Test case 5: Single element (non-zero)
    test5 = [1]
    sol.moveZeroes(test5)
    assert test5 == [1]
    print("Test 5 passed: [1] -> ", test5)
    
    # Test case 6: Zeroes at the end
    test6 = [1, 2, 3, 0, 0]
    sol.moveZeroes(test6)
    assert test6 == [1, 2, 3, 0, 0]
    print("Test 6 passed: [1, 2, 3, 0, 0] -> ", test6)
    
    print("\nAll tests passed!")
