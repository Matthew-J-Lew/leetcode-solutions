"""
Problem: 875 - Koko Eating Bananas
Difficulty: Medium
Topic: Binary Search

Approach:
- Use binary search on Koko’s eating speed `k` (bananas per hour).
- The minimum possible speed is 1 (slowest), and the maximum is max(piles) (fastest possible).
- For each mid value of `k`, compute how many hours it would take for Koko to finish all piles:
    hours = sum(ceil(pile / k) for pile in piles)
- If hours > h, the speed is too slow → shift left boundary up (left = k + 1).
- If hours <= h, the speed works → try smaller speeds by moving right down (right = k - 1).
- When the loop ends, `left` will be the smallest valid eating speed.

Time Complexity: O(n * log(max(piles)))  
Space Complexity: O(1)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # set left as minimum pace k, and right as max pace 
        left = 1
        right = max(piles)

        # Basic binary search loop
        while left <= right:

            # k is mid in this scenario
            k = (left + right) // 2

            # go through each pile and find the amount of hours itd take to eat the bananas (ceiling round up) and sum the total
            hours = sum(math.ceil(pile / k) for pile in piles)

            # if the hours is too high then we increase our speed k
            if hours > h:
                left = k + 1
            
            # if the hours is too low we slow down
            elif hours <= h:
                right = k - 1
        
        # By the end of the loop left will be the minimum valid speed 
        return left