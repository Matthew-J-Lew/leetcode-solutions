"""
Problem: 1929 - Concatenation of Array
Difficulty: Easy
Topic: Arrays

Approach:
- We are asked to return a new array that is the concatenation of the original array with itself.
- In Python, multiplying a list by 2 (`nums * 2`) simply repeats the list twice.
- This gives us the required output directly in O(n) time.

Time Complexity: O(n)   # We copy the list twice, so linear in the size of nums
Space Complexity: O(n)  # We build a new list of size 2n
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
