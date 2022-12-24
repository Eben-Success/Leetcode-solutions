# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # Iterative approah
        # Depth First Search
        
        if not root:
            return 0
        
        stack = [root]
        res = 0
        
        while stack:
            node = stack.pop()
                
            # checks if node is not empty
            if node:
                if low <= node.val <= high:
                    res += node.val
                
                if low < node.val:
                    stack.append(node.left)
                    
                if node.val < high:
                    stack.append(node.right)
                    
        return res
                
        