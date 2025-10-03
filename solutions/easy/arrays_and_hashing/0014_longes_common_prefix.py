"""
Problem: 14 - Longest Common Prefix
Difficulty: Easy
Topic: Strings

Approach:
- Start with the first string as the initial prefix.
- Compare the prefix with each string in the list.
- While the current string does not start with the prefix, 
  shorten the prefix by removing the last character.
- Continue until all strings share the same prefix or the prefix becomes empty.

Time Complexity: O(N * M), where N = number of strings, M = length of the shortest string.
Space Complexity: O(1), only uses constant extra space.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #If the list is empty, no prefix
        if not strs:
            return ""

        #Set the first word as the prefix
        prefix = strs[0]

        #For each word in strs (excluding the first one)
        for word in strs[1:]:

            #Shrink the prefix by 1 character until it matches the start of the word
            while word[:len(prefix)] != prefix:
                #Take off the last character
                prefix = prefix[:-1]
                #If the prefix becomes empty return ""
                if not prefix:
                    return ""
        #Return the final prefix
        return prefix