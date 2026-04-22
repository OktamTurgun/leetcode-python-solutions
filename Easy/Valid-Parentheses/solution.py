"""
Problem: Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)

Description:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Example:
    Input: s = "()"
    Output: true
    
    Input: s = "()[]{}"
    Output: true
    
    Input: s = "([)]"
    Output: false
    Explanation: The brackets are not closed in the correct order.

Approach: Stack
    Use a stack to keep track of opening brackets.
    - When we encounter an opening bracket, push it to the stack.
    - When we encounter a closing bracket, check if it matches the top of the stack.
    - If it matches, pop from the stack. If not, return false.
    - At the end, if the stack is empty, all brackets are valid.

Time Complexity: O(n) - single pass through the string
Space Complexity: O(n) - stack stores up to n/2 opening brackets
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Validate if parentheses/brackets are balanced and correctly ordered.
        
        Args:
            s: String containing parentheses and brackets
            
        Returns:
            True if valid, False otherwise
        """
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Check if stack has matching opening bracket
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            # If it's an opening bracket
            else:
                stack.append(char)
        
        # Stack should be empty if all brackets are matched
        return not stack


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Simple valid parentheses
    assert solution.isValid("()") == True, "'()' should be valid"
    
    # Test 2: Multiple different brackets
    assert solution.isValid("()[]{}") == True, "'()[]{}' should be valid"
    
    # Test 3: Nested brackets
    assert solution.isValid("([{}])") == True, "'([{}])' should be valid"
    
    # Test 4: Invalid order
    assert solution.isValid("([)]") == False, "'([)]' should be invalid (wrong order)"
    
    # Test 5: Missing closing bracket
    assert solution.isValid("([]") == False, "'([' should be invalid (missing closing)"
    
    # Test 6: Extra closing bracket
    assert solution.isValid("()]") == False, "'()]' should be invalid (extra closing)"
    
    # Test 7: Empty string
    assert solution.isValid("") == True, "Empty string should be valid"
    
    # Test 8: Single opening bracket
    assert solution.isValid("(") == False, "'(' should be invalid"
    
    # Test 9: Single closing bracket
    assert solution.isValid(")") == False, "')' should be invalid"
    
    # Test 10: Complex valid case
    assert solution.isValid("{[()]}") == True, "'{[()]}' should be valid"
    
    # Test 11: Only closing brackets
    assert solution.isValid(")))") == False, "'}))' should be invalid"
    
    # Test 12: Mismatched brackets
    assert solution.isValid("(]") == False, "'(]' should be invalid (mismatched)"
    
    print("✅ All test cases passed!")