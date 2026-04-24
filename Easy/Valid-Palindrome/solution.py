class Solution:
    """
    Solution for the Valid Palindrome problem.
    
    This class provides a method to determine if a string is a valid palindrome,
    considering only alphanumeric characters and ignoring case sensitivity.
    """
    
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a string is a valid palindrome, ignoring non-alphanumeric 
        characters and case sensitivity.
        
        Approach:
        - Use two-pointer technique: one starting from left, one from right
        - Skip non-alphanumeric characters on both ends
        - Compare characters case-insensitively
        - If any mismatch found, return False
        - If pointers meet/cross, string is a palindrome
        
        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(1) - only using two pointers
        
        Args:
            s (str): Input string that may contain letters, digits, and special characters
            
        Returns:
            bool: True if string is a valid palindrome, False otherwise
            
        Examples:
            >>> sol = Solution()
            >>> sol.isPalindrome("A man, a plan, a canal: Panama")
            True
            >>> sol.isPalindrome("race a car")
            False
            >>> sol.isPalindrome(" ")
            True
        """
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


def test_is_palindrome():
    """Test cases for the isPalindrome method."""
    sol = Solution()
    
    # Test case 1: Classic palindrome with spaces and punctuation
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
    
    # Test case 2: Not a palindrome
    assert sol.isPalindrome("race a car") == False
    
    # Test case 3: Only spaces
    assert sol.isPalindrome(" ") == True
    
    # Test case 4: Empty string
    assert sol.isPalindrome("") == True
    
    # Test case 5: Single character
    assert sol.isPalindrome("a") == True
    
    # Test case 6: Two same characters
    assert sol.isPalindrome("ab") == False
    
    # Test case 7: Two same characters (palindrome)
    assert sol.isPalindrome("aa") == True
    
    # Test case 8: Only special characters and spaces
    assert sol.isPalindrome(".,") == True
    
    # Test case 9: Numeric palindrome
    assert sol.isPalindrome("12321") == True
    
    # Test case 10: Mixed alphanumeric palindrome
    assert sol.isPalindrome("a1b1a") == True
    
    # Test case 11: Palindrome with multiple spaces and punctuation
    assert sol.isPalindrome("0P") == False
    
    # Test case 12: Case insensitivity check
    assert sol.isPalindrome("Aa") == True
    
    # Test case 13: Complex palindrome
    assert sol.isPalindrome(".,") == True
    
    # Test case 14: Numeric and letters palindrome
    assert sol.isPalindrome("a.b1b.a") == True
    
    # Test case 15: Long palindrome with punctuation
    assert sol.isPalindrome("0P") == False
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_is_palindrome()