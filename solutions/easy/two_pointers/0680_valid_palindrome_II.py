"""
Problem: 680 - Valid Palindrome II
Difficulty: Easy
Topic: Two Pointers / Strings

Approach:
- Use two pointers (`left` and `right`) to compare characters from both ends.
- If characters mismatch, try removing either the left or right character.
- Check if either resulting substring is a palindrome.
- If one of them is, return True; otherwise, return False.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # Helper function that returns if a given string is a palindrome
        def isPalindrome(sub):
            return sub == sub[::-1]

        # Left and right pointers for two pointer approach
        l = 0
        r = len(s) - 1

        # Stop when the pointers meet
        while l < r:
            
            # If there's a mismatch then we call isPalindrome on the cut version of the strings
            if s[l] != s[r]:
                
                # First one is if we skip and delete the left character (l + 1 skips l, and r + 1 includes r)
                # Second one is if we skip and delete the right character (l includes l, and r excludes r)
                return isPalindrome(s[l + 1 : r + 1]) or isPalindrome(s[l : r])
            
            # Increment pointers
            l += 1
            r -= 1
        
        # If we reach the end of the loop that means its a palindrome, return true
        return True
                
