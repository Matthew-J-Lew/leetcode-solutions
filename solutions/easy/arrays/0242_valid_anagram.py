"""
Problem: 242 - Valid Anagram
Difficulty: Easy
Topic: Strings, Hashmap

Approach:
- First check if the lengths of the two strings differ (quick rejection).
- Build frequency tables (hashmaps) for both strings and compare them.
- Alternative optimal approach: use a single fixed-size array of length 26 to count characters.
  Increment counts for string `s` and decrement for string `t`, then verify all counts are zero.

Time Complexity: O(n)  # n = length of the strings
Space Complexity: O(n) for the two-hashmap approach, O(1) for the array approach
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #check if length is different, if its different then they cant possibly be anagrams
        if len(s) != len(t):
            return False

        #Creating hash maps that will act as frequency tables for each character
        nums1 = {}
        nums2 = {}

        #Iterate through each list and create frequency tables
        for char in s:
            if char in nums1:
                nums1[char] += 1
            else:
                nums1[char] = 1
        
        for char in t:
            if char in nums2:
                nums2[char] += 1
            else:
                nums2[char] = 1

        #Return if they are the same or not
        return nums1 == nums2

    #This is the most optimal solution
    def isAnagramCorrect(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Only uses one list and adds/decrements from each letter accordingly
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        #If any of the values are not 0 then its false
        for val in count:
            if val != 0:
                return False
        return True

