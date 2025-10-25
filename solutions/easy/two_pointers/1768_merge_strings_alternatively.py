"""
Problem: 1768 - Merge Strings Alternately
Difficulty: Easy
Topic: Strings, Two Pointers

Approach:
- Use two pointers (i and j) to track positions in word1 and word2.
- Alternately append characters from each string into a result list.
- Continue until both strings are exhausted.
- Join the list into a single string at the end for O(n) efficiency.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # Create an empty list to store the final string
        merged = []
        # Create two pointers
        i, j = 0, 0

        # While at least one of the words still has characters to go through
        while i < len(word1) or j < len(word2):
            
            # If word1 still has characters
            if i < len(word1):
                merged.append(word1[i])
                i += 1
            
            # If word2 still has characters
            if j < len(word2):
                merged.append(word2[j])
                j += 1

        # Join the string and return
        return ''.join(merged)
