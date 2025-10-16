"""
Problem: 74 - Search a 2D Matrix
Difficulty: Medium
Topic: Binary Search

Approach:
- Treat the 2D matrix as one flattened sorted array.
- Perform binary search between 0 and (m * n - 1).
- Use divmod(mid, n) to convert the 1D mid index into 2D coordinates:
    row = mid // n
    col = mid % n
- Compare the middle element with the target:
    - If equal → found, return True
    - If smaller → move left boundary up
    - If larger → move right boundary down
- If not found, return False at the end.

Time Complexity: O(log(m * n))
Space Complexity: O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        if not matrix or not matrix[0]:
            return False

        # Number of rows
        m = len(matrix)
        # Number of columns
        n = len(matrix[0])

        # For the first element in the matrix
        left = 0
        # For the last element in the matrix (- 1 because 0 indexed)
        right = m * n - 1

        # Typical binary search loop
        while left <= right:

            mid = (left + right) // 2

            # divmod returns:
            # row = mid // n, the floor divided row 
            # col = mid % n, the remainder (column)
            row, col = divmod(mid, n)
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False