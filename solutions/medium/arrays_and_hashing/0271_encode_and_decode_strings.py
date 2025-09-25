"""
Problem: 271 - Encode and Decode Strings
Difficulty: Medium
Topic: Strings / Design

Approach:
- For encoding, prepend each string with its length followed by a delimiter (e.g., "4#word").
- Concatenate all encoded parts into one string.
- For decoding, iterate with two pointers:
  - Read characters until the delimiter (#) to get the length.
  - Extract exactly that many characters as the original word.
  - Continue until the end of the string.

Time Complexity: O(N) 
(where N is the total number of characters across all strings, since each char is processed once in encode and decode)

Space Complexity: O(N) 
(for storing the encoded string and the decoded list of strings)
"""
class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedStr = ""

        #Go through each string in the list
        for s in strs:
            #Store the length of the string as well as a # delimiter character with it
            encodedStr += str(len(s)) + "#" + s
        
        #So the returned string will be wordLength#word
        return encodedStr

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        #Loop through the string
        while i < len(s):
            
            #set j as a pointer to the beginning of a word
            j = i
            #while we haven't gotten to a # (or end of the length)
            while s[j] != "#":
                j += 1
            #Extract the number (it would be between i and j)
            length = int(s[i:j])

            #Append the result which is from the first letter to first letter+length = end of the word
            res.append(s[j+1 : j+1+length])

            #increment i to the next word
            i = j + 1 + length
        #return the final list
        return res