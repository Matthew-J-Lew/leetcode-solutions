"""
Problem: 88 - Merge Sorted Array
Difficulty: Easy
Topic: Arrays, Two Pointers

Approach:
- Use three pointers starting from the end of both arrays.
- Compare elements from the back and fill nums1 from the end to avoid overwriting.
- Continue until all elements from nums2 are merged.
- Any leftover nums2 elements are copied into the front of nums1.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Last valid element in nums1
        p1 = m - 1 

        # Last element in nums2
        p2 = n - 1
        
        # Last index of nums1
        p = m + n - 1

        # Loop until one of the pointers is exhausted
        while p1 >= 0 and p2 >= 0:

            # Compare the elements from the back of both the arrays
            if nums1[p1] > nums2[p2]:
                # Place the larger value at the end of nums1
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Placed num2's element at the back of nums1 if nums2's is larger or equal
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are still elements in nums2 then we just add them in
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
