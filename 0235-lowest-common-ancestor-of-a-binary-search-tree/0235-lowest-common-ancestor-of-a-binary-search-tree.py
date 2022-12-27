# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left_val = self.lowestCommonAncestor(root.left, p, q)
        right_val = self.lowestCommonAncestor(root.right, p, q)
        
        if left_val and right_val:
            return root
        
        return left_val if left_val is not None else right_val