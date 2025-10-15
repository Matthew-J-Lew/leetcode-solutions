"""
Problem: 69 - Sqrt(x)
Difficulty: Easy
Topic: Binary Search

Approach:
- Use binary search between 0 and x to find the integer square root.
- Compare mid * mid with x:
    - If equal, mid is the square root.
    - If mid² < x, move left boundary up (left = mid + 1).
    - If mid² > x, move right boundary down (right = mid - 1).
- When the loop ends, right will be the integer part (floor) of the true square root.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Initalize left and right 
        left =  0
        right = x

        # Basic binary search loop
        while left <= right:
            
            # Calculate mid
            mid = (left + right) // 2

            # If mid^2 is x then return mid because its the square root
            if mid * mid == x:
                return mid

            # elif mid^2 is less, then move the left boundary up
            elif mid * mid < x:
                left = mid + 1
            
            # elif mid^2 is higher, then move the right boundary down
            elif mid * mid > x:
                right = mid - 1
        # By the end of the loop the right boundary will be the answer
        return right