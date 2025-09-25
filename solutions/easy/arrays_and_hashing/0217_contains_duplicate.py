"""
Problem: 0217 - Contains Duplicate
Difficulty: Easy
Topic: arrays, hash table

Approach:
- Use a hash set to track seen numbers.
- Iterate through the list:
  - If the number is already in the set, return True (duplicate found).
  - Otherwise, add the number to the set.
- If no duplicates are found after the loop, return False.

Time Complexity: O(n)   # one pass through nums
Space Complexity: O(n)  # storing up to n elements in the set
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create a hash map
        num_map = {}

        # Go through each index and number
        for i, num in enumerate(nums):
            # If the number is already in the list, we have a duplicate
            if num in num_map:
                return True
            # Otherwise we just add the number to the list and continue iterating
            num_map[num] = i
        # If we make it through the entire list and there's no duplicate then return false
        return False

    # This is the best solution
    def hasDuplicate(self, nums: List[int]) -> bool:
        # returns "if the length of the hashmap is smaller than the length of the list" which would imply a duplicate if its true 
        return len(set(nums)) < len(nums)