"""
Problem: 206 - Reverse Linked List
Difficulty: Easy
Topic: Linked List

Approach:
- Use two pointers, `prev` and `curr`. 
- Traverse the list, and for each node, reverse its pointer to point to the previous node.
- Move `prev` and `curr` forward until the end of the list.
- Return `prev` as the new head.

Time Complexity: O(n)    # we visit each node once
Space Complexity: O(1)   # we only use a few pointers
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Previous pointer starts as none
        prev = None
        #Current pointer will start at the head
        curr = head

        #Loop to end of list 
        while curr:
            #Set next as the next node
            nxt = curr.next
            #Reverse the pointer, so the next node becomes the previous one
            curr.next = prev
            #Move prev forward 
            prev = curr
            #Move curr forward
            curr = nxt
        #Prev will now be the new head
        return prev