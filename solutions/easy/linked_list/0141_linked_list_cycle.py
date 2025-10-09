"""
Problem: 141 - Linked List Cycle
Difficulty: Easy
Topic: Linked Lists, Two Pointers

Approach:
- Use two pointers (`slow` and `fast`) starting at the head.
- Move `slow` one step and `fast` two steps at a time.
- If the two pointers ever meet, a cycle exists.
- If `fast` reaches the end (`None`), then there is no cycle.

Time Complexity: O(n)  # Each node is visited at most twice
Space Complexity: O(1) # Only two pointers are used
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Make two pointers start at the beginning of the list
        slow = head
        fast = head

        # Go through the list
        while fast and fast.next:
            # Move slow by one and fast by two
            slow = slow.next
            fast = fast.next.next

            # If they meet, theres a cycle
            if slow == fast:
                return True
        
        # If fast reaches the end, there's no cycle
        return False
