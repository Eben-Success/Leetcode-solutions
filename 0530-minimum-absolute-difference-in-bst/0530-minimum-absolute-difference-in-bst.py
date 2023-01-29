# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        inorder = []
        
        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                inorder.append(node.val)
                inorder_traversal(node.right)
        
        inorder_traversal(root)
        
        min_diff = float("inf")
        
        for i in range(1, len(inorder)):
            min_diff = min(min_diff, inorder[i] - inorder[i-1])
            
        return min_diff
        
        