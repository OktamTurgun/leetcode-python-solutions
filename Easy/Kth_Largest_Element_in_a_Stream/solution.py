"""
Problem: Kth Largest Element in a Stream (https://leetcode.com/problems/kth-largest-element-in-a-stream/)

Description:
    Design a class to find the kth largest element in a stream.
    Implement KthLargest(int k, int[] nums) and int add(int val).

Approach:
    Use a min-heap that stores at most k elements. When the heap grows larger than k,
    remove the smallest element. The root of the heap is always the kth largest element.

Time Complexity:
    - Initialization: O(n log k)
    - Each add operation: O(log k)
Space Complexity:
    O(k)
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        """Initialize the class with k and the initial stream values."""
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """Add a value to the stream and return the current kth largest value."""
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


if __name__ == "__main__":
    # Test 1: Standard stream case
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8
    print("Test 1 passed: KthLargest(3, [4, 5, 8, 2])")

    # Test 2: k = 1 case
    kth_one = KthLargest(1, [2, 3, 4])
    assert kth_one.add(5) == 5
    assert kth_one.add(1) == 5
    print("Test 2 passed: KthLargest(1, [2, 3, 4])")

    # Test 3: Empty stream
    kth_empty = KthLargest(2, [])
    assert kth_empty.add(10) == 10
    assert kth_empty.add(20) == 10
    assert kth_empty.add(50) == 20
    print("Test 3 passed: KthLargest(2, [])")

    print("All tests passed!")