"""
Problem: 0001 - Two Sum
Difficulty: Easy
Topic: arrays, hash table

Approach:
- Iterate through the array while keeping track of seen numbers in a hash map.
- For each number, calculate its complement (target - num).
- If the complement exists in the map, return the indices.
- Otherwise, store the current number and its index in the map.
- This ensures we find the solution in a single pass.

Time Complexity: O(n)  # each number is visited once
Space Complexity: O(n) # storing numbers in the hash map
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a hash map to store the index value pairs
        num_map = {}
        
        # Loop through the list i = index, num = value
        for i, num in enumerate(nums):
            # Complement is the target number - num of current index, so it'd be the remaining number needed to get to the target  
            complement = target - num
            # If the complement is already in our hash map
            if complement in num_map:
                # return the index of the complement thats already in the list and the index 
                return [num_map[complement], i]
            # Else just add a new index value pair to the hash map
            num_map[num] = i
        # Fallback if no solution return false
        return []