"""
Problem: Palindrome Number (https://leetcode.com/problems/palindrome-number/)

Description:
    Given an integer x, return true if x is a palindrome, and false otherwise.
    
Example:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, 
    it becomes 121-. Therefore it is not a palindrome.
    
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Approach:
    Convert the integer to a string and compare it with its reverse.
    Simple and straightforward approach for checking palindromes.

Time Complexity: O(log n) - where n is the number of digits
Space Complexity: O(log n) - for the string representation
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determine if an integer is a palindrome.
        
        Args:
            x: The integer to check
            
        Returns:
            True if x is a palindrome, False otherwise
            
        Raises:
            None
        """
        # Convert number to string
        s = str(x)
        # Compare original with reversed string
        return s == s[::-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Positive palindrome
    assert solution.isPalindrome(121) == True, "121 should be palindrome"
    
    # Test 2: Negative number (not palindrome)
    assert solution.isPalindrome(-121) == False, "-121 should not be palindrome"
    
    # Test 3: Single digit (always palindrome)
    assert solution.isPalindrome(0) == True, "0 should be palindrome"
    
    # Test 4: Single digit positive
    assert solution.isPalindrome(5) == True, "5 should be palindrome"
    
    # Test 5: Non-palindrome (ending with 0)
    assert solution.isPalindrome(10) == False, "10 should not be palindrome"
    
    # Test 6: Large palindrome
    assert solution.isPalindrome(12321) == True, "12321 should be palindrome"
    
    # Test 7: Even-length palindrome
    assert solution.isPalindrome(1221) == True, "1221 should be palindrome"
    
    # Test 8: Non-palindrome
    assert solution.isPalindrome(123) == False, "123 should not be palindrome"
    
    print("All test cases passed!")