"""
Problem: 167 - Two Sum II (Input Array Is Sorted)
Difficulty: Medium
Topic: Two Pointers, Binary Search

Approach:
- Use two pointers: one starting at the beginning, one at the end.
- Move pointers inward depending on whether the current sum is smaller or larger than the target.
- Stop when we find the pair whose sum equals target.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Create two pointers for both ends of the list
        l, r = 0, len(numbers) - 1
        # Create a current sum variable
        curr = 0

        # Loop through the list
        while l < r:
            
            # Calculate the current sum
            curr = numbers[l] + numbers[r]

            # If we found the target, return the indices (1 indexed)
            if curr == target:
                return [(l + 1), (r + 1)]
            
            # If our current sum is too small, move the left pointer up
            elif curr < target:
                l += 1

            # Otherwise our current sum would be too large, so move the right pointer up
            else:
                r -= 1

        # The question assumes there's an answer so we don't return anything at the end
            