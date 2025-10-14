"""
Problem: 374 - Guess Number Higher or Lower
Difficulty: Easy
Topic: Binary Search

Approach:
- Use binary search to efficiently narrow down the guessed number.
- Compare the middle element `mid` to the picked number using the guess API:
  - If guess(mid) == 0 → found the target.
  - If guess(mid) == -1 → our guess is too high, move right boundary down.
  - If guess(mid) == 1 → our guess is too low, move left boundary up.
- Repeat until the number is found.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # Initialize left and right pointers to be 1 and n
        left = 1
        right = n
        
        while left <= right:

            mid = (left + right) // 2

            # If our guess is correct, return the number
            if guess(mid) == 0:
                return mid
            
            # If our guess is too low, we move the left boundary up
            elif guess(mid) == 1:
                left = mid + 1

            # If our guess is too high, we move the right boundary down            
            elif guess(mid) == -1:
                right = mid - 1

        return mid