class Solution:
    """Solution for Remove Element problem."""
    
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Remove all occurrences of a value from the array in-place and return the new length.
        
        The order of elements can be changed, and the elements beyond the new length don't matter.
        
        Args:
            nums: A list of integers
            val: The value to remove
            
        Returns:
            The new length of the array after removing all occurrences of val
            
        Time Complexity: O(n)
        Space Complexity: O(1)
            
        Examples:
            >>> sol = Solution()
            >>> nums = [3, 2, 2, 3]
            >>> k = sol.removeElement(nums, 3)
            >>> k
            2
            >>> nums[:k]
            [2, 2]
        """
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k


if __name__ == "__main__":
    # Test cases
    sol = Solution()
    
    # Test case 1: Basic case
    test1 = [3, 2, 2, 3]
    k1 = sol.removeElement(test1, 3)
    assert k1 == 2
    assert test1[:k1] == [2, 2]
    print(f"Test 1 passed: removeElement([3, 2, 2, 3], 3) returned k={k1}, nums[:k]={test1[:k1]}")
    
    # Test case 2: Remove from beginning
    test2 = [1, 1, 1, 2]
    k2 = sol.removeElement(test2, 1)
    assert k2 == 1
    assert test2[:k2] == [2]
    print(f"Test 2 passed: removeElement([1, 1, 1, 2], 1) returned k={k2}, nums[:k]={test2[:k2]}")
    
    # Test case 3: Value not in array
    test3 = [1, 2, 3]
    k3 = sol.removeElement(test3, 5)
    assert k3 == 3
    assert test3[:k3] == [1, 2, 3]
    print(f"Test 3 passed: removeElement([1, 2, 3], 5) returned k={k3}, nums[:k]={test3[:k3]}")
    
    # Test case 4: Remove all elements
    test4 = [2, 2, 2]
    k4 = sol.removeElement(test4, 2)
    assert k4 == 0
    print(f"Test 4 passed: removeElement([2, 2, 2], 2) returned k={k4}")
    
    # Test case 5: Single element (remove it)
    test5 = [1]
    k5 = sol.removeElement(test5, 1)
    assert k5 == 0
    print(f"Test 5 passed: removeElement([1], 1) returned k={k5}")
    
    # Test case 6: Single element (keep it)
    test6 = [1]
    k6 = sol.removeElement(test6, 2)
    assert k6 == 1
    assert test6[:k6] == [1]
    print(f"Test 6 passed: removeElement([1], 2) returned k={k6}, nums[:k]={test6[:k6]}")
    
    print("\nAll tests passed!")