"""
Problem: 226 - Invert Binary Tree
Difficulty: Easy
Topic: Trees, Recursion

Approach:
- Use recursion (DFS) to swap left and right children of every node.
- Base case: if root is None, return None.
- Recursively call invertTree on the left and right subtrees.

Time Complexity: O(n), where n is the number of nodes (we visit each once)
Space Complexity: O(h), where h is the height of the tree (recursive call stack)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Base case if the root is None, return None
        if not root:
            return None

        # swap the nodes
        root.left, root.right = root.right, root.left

        # recursive call on children
        self.invertTree(root.left)
        self.invertTree(root.right)

        # (this happens at the end of the recursive loop)
        # returns the root 
        return root