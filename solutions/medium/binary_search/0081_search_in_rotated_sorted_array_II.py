"""
Problem: 81 - Search in Rotated Sorted Array II
Difficulty: Medium
Topic: Binary Search

Approach:
- Similar to Problem 33 but handles duplicates.
- If nums[left] == nums[mid] == nums[right], we can’t determine the sorted half.
  → Increment left and decrement right to shrink the search space.
- Otherwise, determine which half is sorted and move the boundaries accordingly.

Time Complexity: O(log n) in average case, but can degrade to O(n) in worst case (all duplicates).
Space Complexity: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left = 0
        right = len(nums) - 1

        #Basic binary search loop
        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # If a duplicate would otherwise stop us from determining which side is sorted
            if nums[left] == nums[mid] == nums[right]:
                # Adjust the pointers by 1 to avoid duplicates
                left += 1
                right -= 1
                continue

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
        # Return false if we can't find it
        return False