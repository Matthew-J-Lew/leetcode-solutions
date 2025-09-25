"""
Problem: 20 - Valid Parentheses
Difficulty: Easy
Topic: Strings / Stack

Approach:
- Use a stack to keep track of opening brackets.
- Create a mapping of closing brackets to their corresponding opening brackets.
- Loop through the string:
    - If the character is a closing bracket, check if the top of the stack has the matching opening bracket:
        - If yes, pop it from the stack.
        - If not, return False (invalid string).
    - If the character is an opening bracket, push it onto the stack.
- At the end, return True only if the stack is empty (all brackets matched correctly).

Time Complexity: O(n) - We process each character once.
Space Complexity: O(n) - In the worst case, the stack can hold all characters if they are all opening brackets.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        #Create empty stack and make a mapping between open brackets and closed brackets
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        #Loop through string
        for char in s:

            #If char is a closing bracket
            if char in mapping:
                #if the stack has at least one element
                #and if the stack's top element is the corresponding open bracket
                if stack and stack[-1] == mapping[char]:
                    #pop the stack to get rid of that pair
                    stack.pop()
                else:
                    #Otherwise there's no corresponding open bracket, return false
                    return False
            #If char is an opening bracket
            else:
                #Add it to the stack
                stack.append(char)

        #Return true if the stack is empty
        return not stack