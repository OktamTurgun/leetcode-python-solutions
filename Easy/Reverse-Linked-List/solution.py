from typing import Optional

class ListNode:
    """
    Definition for singly-linked list node.
    
    Attributes:
        val (int): The value stored in the node
        next (Optional[ListNode]): Reference to the next node in the list
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Solution for reversing a singly linked list.
    
    This class provides a method to reverse a linked list using an iterative approach.
    """
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list.
        
        This method reverses the direction of all links in the linked list,
        so the last node becomes the new head and the original head becomes the tail.
        
        Args:
            head (Optional[ListNode]): The head node of the linked list to reverse.
                                      Can be None for an empty list.
        
        Returns:
            Optional[ListNode]: The new head of the reversed linked list.
                               Returns None if the input list is empty.
        
        Time Complexity: O(n) where n is the number of nodes in the list.
                        We traverse the entire list once.
        
        Space Complexity: O(1) as we only use constant extra space for three pointers.
        
        Example:
            >>> solution = Solution()
            # Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
            >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
            >>> result = solution.reverseList(head)
            # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
        """
        prev = None 
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


# Helper function to convert linked list to list for easy testing
def linked_list_to_list(node: Optional[ListNode]) -> list:
    """Convert a linked list to a Python list for easier assertion in tests."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Helper function to create a linked list from a Python list
def create_linked_list(values: list) -> Optional[ListNode]:
    """Create a linked list from a Python list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Normal list with multiple elements
    print("Test Case 1: Normal list [1, 2, 3, 4, 5]")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseList(head1)
    assert linked_list_to_list(result1) == [5, 4, 3, 2, 1]
    print("✓ PASSED: Reversed to [5, 4, 3, 2, 1]\n")
    
    # Test Case 2: Empty list
    print("Test Case 2: Empty list")
    head2 = None
    result2 = solution.reverseList(head2)
    assert result2 is None
    print("✓ PASSED: Empty list remains None\n")
    
    # Test Case 3: Single element
    print("Test Case 3: Single element [1]")
    head3 = create_linked_list([1])
    result3 = solution.reverseList(head3)
    assert linked_list_to_list(result3) == [1]
    print("✓ PASSED: Single element remains [1]\n")
    
    # Test Case 4: Two elements
    print("Test Case 4: Two elements [1, 2]")
    head4 = create_linked_list([1, 2])
    result4 = solution.reverseList(head4)
    assert linked_list_to_list(result4) == [2, 1]
    print("✓ PASSED: Reversed to [2, 1]\n")
    
    # Test Case 5: Larger list
    print("Test Case 5: Larger list [10, 20, 30, 40, 50, 60, 70]")
    head5 = create_linked_list([10, 20, 30, 40, 50, 60, 70])
    result5 = solution.reverseList(head5)
    assert linked_list_to_list(result5) == [70, 60, 50, 40, 30, 20, 10]
    print("✓ PASSED: Reversed to [70, 60, 50, 40, 30, 20, 10]\n")
    
    # Test Case 6: Negative numbers
    print("Test Case 6: List with negative numbers [-1, -2, -3]")
    head6 = create_linked_list([-1, -2, -3])
    result6 = solution.reverseList(head6)
    assert linked_list_to_list(result6) == [-3, -2, -1]
    print("✓ PASSED: Reversed to [-3, -2, -1]\n")
    
    # Test Case 7: Mixed positive and negative
    print("Test Case 7: Mixed numbers [-5, 0, 5, 10]")
    head7 = create_linked_list([-5, 0, 5, 10])
    result7 = solution.reverseList(head7)
    assert linked_list_to_list(result7) == [10, 5, 0, -5]
    print("✓ PASSED: Reversed to [10, 5, 0, -5]\n")
    
    print("=" * 50)
    print("All test cases passed successfully! ✓")
    print("=" * 50)