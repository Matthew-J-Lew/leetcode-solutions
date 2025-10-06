"""
Problem: 169 - Majority Element
Difficulty: Easy
Topic: Hashmap / Counting

Approach:
- Use a hashmap (dictionary) to count the frequency of each element in nums.
- As we count, if any element’s frequency exceeds n/2, return it immediately.
- This works because the majority element is guaranteed to exist.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #Create a hash map to use as a frequency table
        nums_map = {}
    
        # loop through the list
        for num in nums:
            
            #logic for tracking count of a number
            if num in nums_map:
                nums_map[num] = nums_map[num] + 1
            else:
                nums_map[num] = 1
        
            #if the count is greater than half, return
            if nums_map[num] > len(nums) / 2:
                return num