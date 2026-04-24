class Solution:
  """
  Solution for the Longest Common Prefix problem.
  
  This class provides a method to find the longest common prefix
  shared by all strings in a list.
  """
  
  def longestCommonPrefix(self, strs: list[str]) -> str:
    """
    Find the longest common prefix of a list of strings.
    
    Approach:
    - Use the first string as the initial prefix
    - Iterate through remaining strings and trim the prefix
      until each string starts with the current prefix
    - Return the resulting prefix or empty string if no common prefix exists
    
    Time Complexity: O(S) where S is the sum of all characters in all strings
    Space Complexity: O(1) excluding the output
    
    Args:
        strs (list[str]): A list of strings
        
    Returns:
        str: The longest common prefix string, or empty string if there's no common prefix
        
    Examples:
        >>> sol = Solution()
        >>> sol.longestCommonPrefix(["flower", "flow", "flight"])
        'fl'
        >>> sol.longestCommonPrefix(["dog", "racecar", "car"])
        ''
    """
    if not strs:
      return ""
    
    prefix = strs[0]

    for i in range(1, len(strs)):
      while not strs[i].startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
          return ""
    return prefix


def test_longest_common_prefix():
    """Test cases for the longestCommonPrefix method."""
    sol = Solution()
    
    # Test case 1: Common prefix exists
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    
    # Test case 2: No common prefix
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    
    # Test case 3: Single string
    assert sol.longestCommonPrefix(["hello"]) == "hello"
    
    # Test case 4: Empty list
    assert sol.longestCommonPrefix([]) == ""
    
    # Test case 5: Entire string is prefix
    assert sol.longestCommonPrefix(["abc", "abc", "abc"]) == "abc"
    
    # Test case 6: One character prefix
    assert sol.longestCommonPrefix(["a", "ac", "ab"]) == "a"
    
    # Test case 7: Empty string in list
    assert sol.longestCommonPrefix(["abc", ""]) == ""
    
    # Test case 8: Two strings with common prefix
    assert sol.longestCommonPrefix(["prefix", "prepare"]) == "pre"
    
    # Test case 9: No common prefix with single character strings
    assert sol.longestCommonPrefix(["x", "y", "z"]) == ""
    
    # Test case 10: All strings are identical
    assert sol.longestCommonPrefix(["test", "test", "test"]) == "test"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_common_prefix()