"""
Problem: 36 - Valid Sudoku
Difficulty: Medium
Topic: Arrays / Hashing

Approach:
- Use 3 hash sets for each row, column, and 3x3 box.
- As you loop through the board, skip empty cells.
- For each filled cell, check if the number already exists in its row, column, or box.
- If it does, return False immediately.
- Otherwise, record the number in the corresponding sets.
- If no conflicts are found after scanning the whole board, return True.

Time Complexity: O(1) 
# (Always a fixed 9x9 board → 81 operations max, treated as constant time)
Space Complexity: O(1) 
# (At most 81 entries stored across sets, still constant because the board size is fixed)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Creating 9 sets for rows, cols, boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        #Loop through each cell on the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                #Skip empty cells
                if val == '.':
                    continue

                #Find which 3x3 box this cell belongs to 
                box_idx = (r // 3) * 3 + (c // 3)

                #If the value is already in the row, col, or box return false
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False

                #Update to record the value
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        #If its not invalid, return true.       
        return True