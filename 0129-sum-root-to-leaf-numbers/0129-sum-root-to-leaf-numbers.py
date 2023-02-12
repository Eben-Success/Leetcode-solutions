# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def sumNumbersHelper(root, num):
            if root is None:
                return 0
            
            num = num * 10 + root.val
            
            if root.left is None and root.right is None:
                return num
            
            return sumNumbersHelper(root.left, num) + sumNumbersHelper(root.right, num)
        
        return sumNumbersHelper(root, 0)