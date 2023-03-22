# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # bfs
        
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0
        
        
        while stack:
            node, count = stack.pop()
            
            
            if node.left is None and node.right is None:
                max_depth = max(count, max_depth)
                
            if node.left:
                stack.append((node.left, count + 1))
                
            if node.right:
                stack.append((node.right, count + 1))
                
        return max_depth
        