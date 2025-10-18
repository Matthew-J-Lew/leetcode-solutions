"""
Problem: 1011 - Capacity to Ship Packages Within D Days
Difficulty: Medium
Topic: Binary Search

Approach:
- Use binary search to find the minimal ship capacity `w` that allows shipping within the given days.
- The lower bound (`left`) is the heaviest single package, since the ship must carry it.
- The upper bound (`right`) is the sum of all package weights, representing carrying all in one day.
- For each candidate capacity `w`, simulate the shipping process:
  - Add weights one by one until exceeding `w`, then start a new day.
  - Count how many days are needed.
- If the number of days exceeds the limit, increase capacity (move `left` up).
- Otherwise, try smaller capacities (move `right` down).
- At the end, `left` will represent the smallest capacity sufficient to ship within the deadline.

Time Complexity: O(n log(sum(weights)))
Space Complexity: O(1)
"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Left is the highest single item in weights because we need to lift it at some point
        left = max(weights)
        # Right is the sum of all the weights as if we were able to carry it all in one day
        right = sum(weights)

        # Basic binary search loop 
        while left <= right:

            # Calculate our mid value, the theoretical ship capacity
            w = (left + right) // 2

            # Set days needed as minimum 1
            days_needed = 1
            # Set the current weight as 0
            current_weight = 0

            # Go through each weight
            for weight in weights:

                # If we would go over the ship's weight limit
                if current_weight + weight > w:
                    # Increase the days needed because we need another day 
                    days_needed += 1
                    # Set the current weight back to 0 
                    current_weight = 0
                # Otherwise increment the current weight by weight
                current_weight += weight
            
            # If the days we needed with the given w value was too much, move the left boundary up
            if days_needed > days:
                left = w + 1
            # If the days we needed with the given w value was too little or the same, move the right boundary down
            else:
                right = w - 1

        # By the end of the loop the left pointer is our finished value
        return left