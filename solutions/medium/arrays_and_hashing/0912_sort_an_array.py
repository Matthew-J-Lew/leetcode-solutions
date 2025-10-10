"""
Problem: 912 - Sort an Array
Difficulty: Medium
Topic: Sorting, Divide and Conquer

Approach:
- Use the merge sort algorithm.
- Recursively divide the array into halves until single elements remain.
- Merge sorted halves by comparing elements from both lists in order.
- This guarantees O(n log n) time complexity.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Base case — single element or empty array is already sorted
        if len(nums) <= 1:
            return nums

        # Split into two halves
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0

        # Compare elements from left and right lists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Add any remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged
