"""
Problem: 35 - Search Insert Position
Difficulty: Easy
Topic: Binary Search

Approach:
- Use binary search to efficiently find the target's position.
- If the target is found, return its index.
- If not found, the 'left' pointer will represent the correct insertion index
  to maintain sorted order.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Initiate left and right sides of the list
        left = 0
        right = len(nums) - 1

        # While our pointers haven't crossed over each other
        while left <= right:
            
            # Find middle index between pointers
            mid = (left + right) // 2

            # If we've found the target, return the index
            if nums[mid] == target:
                return mid
            
            # Else if we're too short, then move the left pointer to the midpoint + 1
            elif nums[mid] < target:
                left = mid + 1
            # Else if we're too big, then move the right pointer to the midpoint - 1
            else:
                right = mid - 1
        # Return left as it is the 'would be' correct insertion point
        return left