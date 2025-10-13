"""
Problem: 704 - Binary Search  
Difficulty: Easy  
Topic: Arrays / Binary Search  

Approach:
- Use two pointers (`left` and `right`) to define the search range.  
- Repeatedly find the middle index and compare the middle value to the target.  
- If the middle value equals the target, return its index.  
- If the middle value is smaller, move the left pointer to `mid + 1` to search the right half.  
- If the middle value is larger, move the right pointer to `mid - 1` to search the left half.  
- Continue until `left` passes `right`, meaning the target is not found.

Time Complexity: O(log n)  
Space Complexity: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Initiate left and right side of the list
        left = 0
        right = len(nums) - 1

        # While we haven't met in the middle
        while left <= right:

            # Find middle of the list
            mid = (left + right) // 2

            # If the middle of the list is the target, return it
            if nums[mid] == target:
                return mid

            # If the middle of the list is less than the target, then we move the left pointer to the middle + 1 (search the right side)
            elif nums[mid] < target:
                left = mid + 1
            
            # Otherwise we move the right pointer to the middle - 1 (search the left side)
            else:
                right = mid - 1
        
        # Loop is at it's end, return -1
        return -1