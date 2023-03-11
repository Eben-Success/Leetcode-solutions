# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val
        
        left = self.checkTree(root.left)
        right = self.checkTree(root.right)
        
        return True if (left + right) == root.val else False
            
        
        