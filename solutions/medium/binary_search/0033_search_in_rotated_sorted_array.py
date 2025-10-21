"""
Problem: 33 - Search in Rotated Sorted Array
Difficulty: Medium
Topic: Binary Search

Approach:
- Perform a modified binary search:
  - One of the halves (left or right) is always sorted.
  - Check which half is sorted and whether the target lies within that range.
  - Adjust search boundaries accordingly.
- Continue until target is found or search space is empty.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        #Basic binary search loop
        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # This means the left side of the list is sorted
            if nums[left] <= nums[mid]:
                # Binary search tactic, bring the right pointer down
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Bring the left pointer up
                else:
                    left = mid + 1

            # Otherwise the right side of the list must be sorted
            else:
                # Bring the left pointer up
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Bring the right pointer down
                else:
                    right = mid - 1
        # Return -1 if we can't find it
        return -1
