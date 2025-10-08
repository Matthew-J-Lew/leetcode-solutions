"""
Problem: 344 - Reverse String
Difficulty: Easy
Topic: Strings / Two Pointers

Approach:
- Use two pointers (`left` and `right`) starting at the beginning and end of the list.
- Swap the characters at these pointers and move them toward each other.
- Continue until the pointers meet in the middle, effectively reversing the list in-place.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left, right = 0, len(s) - 1

        # Swap elements until pointers meet
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
