"""
Problem: 125 - Valid Palindrome
Difficulty: Easy
Topic: Strings / Two Pointers

Approach:
- First approach: Clean the string by filtering only alphanumeric characters 
  and converting them to lowercase, then check if the cleaned string equals its reverse.
- Optimized approach: Use two pointers (one at the start, one at the end), 
  skip non-alphanumeric characters, and compare characters while moving inward. 
  This avoids building a new string and saves space.

Time Complexity: O(n)   # n is the length of the string
Space Complexity: O(n)  # for the cleaned string approach
Space Complexity: O(1)  # for the two-pointer approach
"""
class Solution:

    def isPalindrome(self, s: str) -> bool:
        #Create new placeholder string
        newString = ""
        #Loop through the string
        for char in s:
            #If its an alphanumeric character then add the lowercase to the new string
            if char.isalnum():
                newString = newString + char.lower()
        #Return if the string is same in reverse
        return newString == newString[::-1]


    #This is the more refined, space efficient version
    def isPalindrome2Pointer(self, s: str) -> bool:
        #two pointers, one at beginning, one at end of string
        l, r = 0, len(s) - 1

        #while the pointers have not crossed
        while l < r:
            #if there is a non alphanumeric character then we skip it
            while l < r and not s[l].isalnum():
                l += 1
            #if there is a non alphanumeric character then we skip it
            while r > l and not s[r].isalnum():
                r -= 1
            #if the corresponding left and right characters dont match then we return false
            if s[l].lower() != s[r].lower():
                return False
            #Otherwise iterate again
            l, r = l + 1, r - 1
        #If we get through the entire string then that means its true
        return True
