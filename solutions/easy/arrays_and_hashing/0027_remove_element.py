"""
Problem: 27 - Remove Element
Difficulty: Easy
Topic: Arrays / Two Pointers

Approach:
- Use a two-pointer method.
- One pointer (i) iterates through the array.
- The other pointer (k) tracks the position where the next non-val element should go.
- Whenever nums[i] is not equal to val, copy nums[i] to nums[k] and increment k.
- At the end, k represents how many valid elements remain.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to track the position for the next valid element
        k = 0

        # Loop through the array
        for i in range(len(nums)):
            # If nums[i] is not the value we want to remove
            if nums[i] != val:
                # Move it to the next valid spot
                nums[k] = nums[i]
                # Increment k to the next slot
                k += 1

        # Return the number of valid elements
        return k
