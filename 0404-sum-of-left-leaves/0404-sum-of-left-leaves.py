# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
#         if not root:
#             return 0
        
#         left_sum = 0
        
#         # Check if the left child is a leaf node
#         if root.left and not root.left.left and not root.left.right:
#             left_sum += root.left.val
        
#         left_sum += self.sumOfLeftLeaves(root.left)
#         left_sum += self.sumOfLeftLeaves(root.right)
        
#         return left_sum
    
    
        if not root:
            return 0
        
        left_sum = 0
        
        stack = [(root, False)]
        
        while stack:
            node, is_left = stack.pop()
            
            if not node.left and not node.right and is_left:
                left_sum += node.val
                
            if node.right:
                stack.append((node.right, False))
                
            if node.left:
                stack.append((node.left, True))
                
        return left_sum
                