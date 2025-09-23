"""
Problem: 347 - Top K Frequent Elements
Difficulty: Medium
Topic: arrays, hash map, sorting, heap

Approach:
- Build a frequency table (hash map) to count how many times each number appears.
- Convert the frequency table into a list of (num, frequency) pairs.
- Sort this list by frequency in descending order.
- Extract the first k numbers from the sorted list and return them.

Time Complexity: O(n log n)   # building the map is O(n), sorting is O(m log m), where m is unique elements (<= n)
Space Complexity: O(n)        # hash map + list of pairs
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Create an empty hash map to make a freuency table
        nums_map = {}

        #Loop through the list
        for i, num in enumerate(nums):
            
            #If the number is not in the nums map yet make a new entry in the table
            if num not in nums_map:
                nums_map[num] = 0
            #Increment the table entry by 1
            nums_map[num] = nums_map[num] + 1

        #Turn the map into a list of pairs of num, frequency pairs
        pairs = list(nums_map.items())
        #Sort the lists elements based on the frequency of each pair and reverse it 
        pairs.sort(key=lambda x: x[1], reverse=True)
        #The result is a list of just the numbers not frequencies, and cut off the list at the kth position
        result = [num for num, freq in pairs[:k]]
        return result