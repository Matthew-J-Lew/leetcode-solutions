"""
Problem: 153 - Find Minimum in Rotated Sorted Array
Difficulty: Medium
Topic: Binary Search

Approach:
- Use binary search to find the pivot point (minimum element).
- Compare middle element to the rightmost element:
  - If nums[mid] > nums[right], the minimum lies to the right.
  - Else, the minimum lies at mid or to the left.
- Continue until left == right, which will point to the minimum.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        # Basic binary search condition 
        while left < right:

            # Assign our mid value
            mid = (left + right) // 2

            # If the number in the middle is bigger than the one on the right, then that means the minimum is to the right, and we move the left pointer up
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise the minimum is on the left side so we move the right boundary down
            else:
                right = mid
                
        # By the end of the loop, nums[left] will be the minimum
        return nums[left]