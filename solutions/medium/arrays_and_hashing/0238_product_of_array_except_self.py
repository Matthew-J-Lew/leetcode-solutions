"""
Problem: 238 - Product of Array Except Self
Difficulty: Medium
Topic: Arrays / Prefix & Postfix Products

Approach:
- Use a result array initialized with 1s.
- First pass (left to right): build prefix products (everything to the left of i).
- Second pass (right to left): multiply by postfix products (everything to the right of i).
- This way, each index ends up with the product of all elements except itself, without using division.

Time Complexity: O(n)   # one forward pass + one backward pass
Space Complexity: O(1)  # ignoring the output array (only prefix and postfix scalars are used)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Create a res list the same length as nums
        res = [1] * len(nums)

        #Create a prefix that represents the product of all the items before it
        prefix = 1

        #loop through nums
        for i in range(len(nums)):
            #Set the result of index as prefix (product of elements before i)
            res[i] = prefix
            #Increase prefixes value by multiplying it by nums[i]
            prefix *= nums[i]

        #Create a postfix that represents the product of all the items after it
        postfix = 1
        #Loop backwards through nums
        for i in range(len(nums) - 1, -1, -1):
            #Multiply res i by postfix
            res[i] *= postfix
            #Increases postfix value by multiplying it by nums[i] (note we're going down instead of up this time)
            postfix *= nums[i]

        #Return result
        return res
