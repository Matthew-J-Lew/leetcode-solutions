"""
Problem: 21 - Merge Two Sorted Lists
Difficulty: Easy
Topic: Linked List

Approach:
- Use a dummy node (`finalList`) to simplify list construction.
- Maintain a `tail` pointer to keep track of the current end of the merged list.
- Traverse both lists while they are non-empty:
    - Attach the smaller value node to `tail.next`.
    - Advance the pointer of the list from which the node was taken.
    - Move `tail` forward.
- After one list ends, attach the remainder of the other list.
- Return `finalList.next` as the head of the merged list.

Time Complexity: O(n + m), where n and m are the lengths of the two lists.
Space Complexity: O(1), since merging is done in-place using pointers.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Create a final list to return and act as list head
        finalList = ListNode()
        #Tail pointer that will begin building the new list
        tail = finalList

        #While both lists are still populated
        while list1 and list2:
            #If the value of list1 is less than or equal to list2
            if list1.val <= list2.val:
                #Add list1's item to the list
                tail.next = list1
                #Iterate list1 to the next spot
                list1 = list1.next
            #Otherwise add list 2's item to the list
            else:
                tail.next = list2
                #Iterate list2 to the next spot
                list2 = list2.next
            #Move the tail pointer forward
            tail = tail.next

        #If there's anything left in either of the lists, add it
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        #Return the final list
        return finalList.next