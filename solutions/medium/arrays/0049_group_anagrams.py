"""
Problem: 49 - Group Anagrams
Difficulty: Medium
Topic: Strings / Hash Map

Approach:
- Use a hashmap (dictionary) to group strings by their "anagram key".
- For each string:
    - Sort the string to generate a key that is identical for all anagrams.
    - If the key is not in the hashmap, create a new list for it.
    - Append the string to the corresponding list.
- At the end, return all the lists of grouped anagrams from the hashmap.

Time Complexity: O(n * k log k) 
    # n = number of strings, k = maximum length of a string (sorting each string takes O(k log k))
Space Complexity: O(n * k) 
    # storing all strings in the hashmap
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Initialize empty hash map
        anagramMap = {}

        # Loop through the strings
        for string in strs:
            
            # Sort the current string and set it as a key for the hash map
            key = ''.join(sorted(string))

            # If the key is not already in the map, then it's a new entry
            if key not in anagramMap:
                anagramMap[key] = []

            # Add the string to the list for the corresponding key
            anagramMap[key].append(string)

        # Return all grouped anagrams
        return list(anagramMap.values())
