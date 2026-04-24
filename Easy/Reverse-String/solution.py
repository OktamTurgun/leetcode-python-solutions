class Solution:
    """
    Solution for the Reverse String problem.
    
    This class provides a method to reverse a list of characters in-place
    without using extra space for another array.
    """
    
    def reverseString(self, s: list[str]) -> None:
        """
        Reverse a list of characters in-place.
        
        Approach:
        - Use two-pointer technique: one starting from the beginning,
          one from the end
        - Swap characters at both pointers
        - Move pointers towards the center until they meet
        - Modifies the list in-place without returning anything
        
        Time Complexity: O(n) where n is the length of the list
        Space Complexity: O(1) - only using two pointers, in-place modification
        
        Args:
            s (list[str]): A list of characters to be reversed in-place
            
        Returns:
            None: The function modifies the list in-place
            
        Examples:
            >>> sol = Solution()
            >>> s = ["H","e","l","l","o"]
            >>> sol.reverseString(s)
            >>> s
            ["o","l","l","e","H"]
            >>> s = ["h","a"]
            >>> sol.reverseString(s)
            >>> s
            ["a","h"]
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


def test_reverse_string():
    """Test cases for the reverseString method."""
    sol = Solution()
    
    # Test case 1: Basic string reversal
    s = ["H", "e", "l", "l", "o"]
    sol.reverseString(s)
    assert s == ["o", "l", "l", "e", "H"]
    
    # Test case 2: Two character string
    s = ["h", "a"]
    sol.reverseString(s)
    assert s == ["a", "h"]
    
    # Test case 3: Single character
    s = ["a"]
    sol.reverseString(s)
    assert s == ["a"]
    
    # Test case 4: Empty list
    s = []
    sol.reverseString(s)
    assert s == []
    
    # Test case 5: Two identical characters
    s = ["a", "a"]
    sol.reverseString(s)
    assert s == ["a", "a"]
    
    # Test case 6: Numbers as characters
    s = ["1", "2", "3", "4", "5"]
    sol.reverseString(s)
    assert s == ["5", "4", "3", "2", "1"]
    
    # Test case 7: Mixed characters
    s = ["a", "1", "b", "2", "c"]
    sol.reverseString(s)
    assert s == ["c", "2", "b", "1", "a"]
    
    # Test case 8: Special characters
    s = ["!", "@", "#", "$"]
    sol.reverseString(s)
    assert s == ["$", "#", "@", "!"]
    
    # Test case 9: Spaces
    s = ["a", " ", "b"]
    sol.reverseString(s)
    assert s == ["b", " ", "a"]
    
    # Test case 10: Long string
    s = list("abcdefghij")
    sol.reverseString(s)
    assert s == list("jihgfedcba")
    
    # Test case 11: Odd length string
    s = ["a", "b", "c"]
    sol.reverseString(s)
    assert s == ["c", "b", "a"]
    
    # Test case 12: Even length string
    s = ["a", "b", "c", "d"]
    sol.reverseString(s)
    assert s == ["d", "c", "b", "a"]
    
    # Test case 13: Palindrome remains same
    s = ["a", "b", "a"]
    sol.reverseString(s)
    assert s == ["a", "b", "a"]
    
    # Test case 14: Same character repeated
    s = ["x", "x", "x", "x"]
    sol.reverseString(s)
    assert s == ["x", "x", "x", "x"]
    
    # Test case 15: Uppercase and lowercase
    s = ["A", "b", "C", "d"]
    sol.reverseString(s)
    assert s == ["d", "C", "b", "A"]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_reverse_string()