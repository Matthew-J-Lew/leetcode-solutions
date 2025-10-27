"""
Problem: 26 - Remove Duplicates from Sorted Array
Difficulty: Easy
Topic: Arrays / Two Pointers

Approach:
- Use a two-pointer technique since the array is already sorted.
- One pointer (i) scans the array, while another (k) tracks the next position 
  to place a unique element.
- Whenever we find a new unique value (nums[i] != nums[i - 1]), 
  we copy it to nums[k] and move k forward.
- This ensures that the first k elements of nums contain all unique numbers.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        # Our pointer for unique element positions
        k = 1

        # Loop through the array 
        for i in range(1, len(nums)):
            
            # If the current number is different from the previous, it is unique
            if nums[i] != nums[i - 1]:
                # Overwrite position k as nums[i] (it will now be the first element in the array)
                nums[k] = nums[i]
                # Move onto the next position k to update
                k += 1
                
        # Return k
        return k