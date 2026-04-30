"""
Merge Two Sorted Lists

This module contains a solution to merge two sorted linked lists into a single
sorted linked list.

Problem: Given two sorted linked lists list1 and list2, merge them into one
sorted list and return the head of the merged list.
"""

from typing import Optional


class ListNode:
    """A node in a singly linked list."""
    
    def __init__(self, val=0, next=None):
        """
        Initialize a ListNode.
        
        Args:
            val (int): The value stored in the node. Defaults to 0.
            next (Optional[ListNode]): Reference to the next node. Defaults to None.
        """
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.
        
        Merges two sorted singly linked lists by comparing nodes from both lists
        and appending the smaller node to the result list. Uses a dummy node to
        simplify the merging process.
        
        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.
        
        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        
        Time Complexity: O(n + m) where n and m are the lengths of list1 and list2.
        Space Complexity: O(1) as we only use a constant amount of extra space.
        
        Example:
            >>> # Example 1: list1 = [1,2,4], list2 = [1,3,4]
            >>> # Return: [1,1,2,3,4,4]
            
            >>> # Example 2: list1 = [], list2 = [0]
            >>> # Return: [0]
        """
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        return dummy.next


def create_linked_list(values: list) -> Optional[ListNode]:
    """
    Helper function to create a linked list from a list of values.
    
    Args:
        values (list): List of integer values.
    
    Returns:
        Optional[ListNode]: The head of the created linked list.
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list:
    """
    Helper function to convert a linked list to a list of values.
    
    Args:
        head (Optional[ListNode]): The head of the linked list.
    
    Returns:
        list: List of values from the linked list.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Both lists have elements
    print("Test Case 1: Merge [1,2,4] and [1,3,4]")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    result_list = linked_list_to_list(result)
    print(f"Result: {result_list}")
    assert result_list == [1, 1, 2, 3, 4, 4], "Test Case 1 failed"
    print("✓ Test Case 1 passed\n")
    
    # Test Case 2: First list is empty
    print("Test Case 2: Merge [] and [0]")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    result_list = linked_list_to_list(result)
    print(f"Result: {result_list}")
    assert result_list == [0], "Test Case 2 failed"
    print("✓ Test Case 2 passed\n")
    
    # Test Case 3: Both lists are empty
    print("Test Case 3: Merge [] and []")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    result_list = linked_list_to_list(result)
    print(f"Result: {result_list}")
    assert result_list == [], "Test Case 3 failed"
    print("✓ Test Case 3 passed\n")
    
    # Test Case 4: First list is longer
    print("Test Case 4: Merge [1,2,3,4,5] and [1,3]")
    list1 = create_linked_list([1, 2, 3, 4, 5])
    list2 = create_linked_list([1, 3])
    result = solution.mergeTwoLists(list1, list2)
    result_list = linked_list_to_list(result)
    print(f"Result: {result_list}")
    assert result_list == [1, 1, 2, 3, 3, 4, 5], "Test Case 4 failed"
    print("✓ Test Case 4 passed\n")
    
    # Test Case 5: Second list is longer
    print("Test Case 5: Merge [1] and [2,3,4,5,6]")
    list1 = create_linked_list([1])
    list2 = create_linked_list([2, 3, 4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    result_list = linked_list_to_list(result)
    print(f"Result: {result_list}")
    assert result_list == [1, 2, 3, 4, 5, 6], "Test Case 5 passed"
    print("✓ Test Case 5 passed\n")
    
    # Test Case 6: Lists with duplicate values
    print("Test Case 6: Merge [1,1,1] and [2,2,2]")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([2, 2, 2])
    result = solution.mergeTwoLists(list1, list2)
    result_list = linked_list_to_list(result)
    print(f"Result: {result_list}")
    assert result_list == [1, 1, 1, 2, 2, 2], "Test Case 6 failed"
    print("✓ Test Case 6 passed\n")
    
    # Test Case 7: Negative numbers
    print("Test Case 7: Merge [-4,-1,0] and [-2,1,3]")
    list1 = create_linked_list([-4, -1, 0])
    list2 = create_linked_list([-2, 1, 3])
    result = solution.mergeTwoLists(list1, list2)
    result_list = linked_list_to_list(result)
    print(f"Result: {result_list}")
    assert result_list == [-4, -2, -1, 0, 1, 3], "Test Case 7 failed"
    print("✓ Test Case 7 passed\n")
    
    print("=" * 40)
    print("All test cases passed! ✓")
    print("=" * 40)