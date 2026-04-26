class Solution:
    """Solution for Move Element To End problem."""
    
    def removeElementToEnd(self, array: list[int], toMove: int) -> list[int]:
        """
        Move all occurrences of a value to the end of the array.
        
        Args:
            array: List of integers
            toMove: The value to move to the end
            
        Returns:
            The modified array with the target value at the end
            
        Examples:
            >>> sol = Solution()
            >>> sol.removeElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2)
            [1, 3, 4, 2, 2, 2, 2, 2]
        """
        left = 0

        # Move all non-toMove elements to the left
        for right in range(len(array)):
            if array[right] != toMove:
                array[left] = array[right]
                left += 1
        
        # Fill the rest with toMove elements
        while left < len(array):
            array[left] = toMove
            left += 1
        
        return array


if __name__ == "__main__":
    # Test cases
    sol = Solution()
    
    # Test case 1: Basic case
    test1 = [2, 1, 2, 2, 2, 3, 4, 2]
    result1 = sol.removeElementToEnd(test1, 2)
    assert result1 == [1, 3, 4, 2, 2, 2, 2, 2]
    print("Test 1 passed: [2, 1, 2, 2, 2, 3, 4, 2] -> ", result1)
    
    # Test case 2: All same elements
    test2 = [1, 1, 1, 1]
    result2 = sol.removeElementToEnd(test2, 1)
    assert result2 == [1, 1, 1, 1]
    print("Test 2 passed: [1, 1, 1, 1] -> ", result2)
    
    # Test case 3: No target element
    test3 = [1, 2, 3, 4]
    result3 = sol.removeElementToEnd(test3, 5)
    assert result3 == [1, 2, 3, 4]
    print("Test 3 passed: [1, 2, 3, 4] -> ", result3)
    
    # Test case 4: Single element array
    test4 = [1]
    result4 = sol.removeElementToEnd(test4, 1)
    assert result4 == [1]
    print("Test 4 passed: [1] -> ", result4)
    
    print("\nAll tests passed!")