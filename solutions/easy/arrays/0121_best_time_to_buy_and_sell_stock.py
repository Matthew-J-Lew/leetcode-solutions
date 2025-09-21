"""
Problem: 121 - Best Time to Buy and Sell Stock
Difficulty: Easy
Topic: Arrays, Dynamic Programming

Approach:
- Track the lowest price seen so far (`low`).
- At each day, compute potential profit as `price - low` (as if selling today).
- Update `profit` if the current day's profit is greater than the best seen so far.
- One-pass solution ensures efficiency.

Time Complexity: O(n)  # iterate through the prices once
Space Complexity: O(1) # only a few scalar variables are used
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Creating variables 
        low = prices[0] 
        high = 0
        profit = 0

        #Pass through the list
        for i in prices:
            
            #If there's a new low, make it the new low/starting point and reset the high tracker since we're starting again
            if i < low:
                low = i
                high = 0

            #If there's a higher high set it as high
            if i > high:
                high = i

            #Update profit if theres a higher profit presented by high
            if high - low > profit:
                profit = high - low
        
        #Return final profit
        return profit
    
    def maxProfitBest(self, prices: List[int]) -> int:
        
        #Make a low and a profit variable
        low = prices[0]
        profit = 0

        #Iterate through the list
        for price in prices:
            #If the current index is a new low
            if price < low:
                #Set low as the new price/starting point
                low = price
            #Set profit as the max between profit (our current profit) and price - low, so high would be price in this case 
            profit = max(profit, price - low)
        
        #Return final profit
        return profit



