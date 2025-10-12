"""
Problem: 75 - Sort Colors
Difficulty: Easy
Topic: Arrays

Approach:
- Use the Dutch National Flag algorithm with three pointers: low, mid, high.
- low: boundary for 0s (reds). mid: current index being inspected. high: boundary for 2s (blues).
- Iterate while mid <= high:
  - If nums[mid] == 0: swap nums[low] and nums[mid]; increment low and mid.
  - If nums[mid] == 1: just increment mid.
  - If nums[mid] == 2: swap nums[mid] and nums[high]; decrement high.
- This sorts in-place in one pass.

Time Complexity: O(n)   # one pass through the array
Space Complexity: O(1)  # constant extra space
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Create three pointers to go through the list with
        low, mid, high = 0, 0, len(nums) - 1

        # Until the mid passes the high
        while mid <= high:
            # If we have a 0, swap the current element with the low pointer
            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            
            # Otherwise if it is 1, it is already in the right place so increment by 1
            elif nums[mid] == 1:
                mid += 1
            
            # If it is 2 then swap the current element with the high pointer
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1