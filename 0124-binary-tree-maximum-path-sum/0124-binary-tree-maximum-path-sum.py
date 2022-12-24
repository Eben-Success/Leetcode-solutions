# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        self.max_path_sum = root.val
        self.dfs(root)
        return self.max_path_sum
    
    
    def dfs(self, node):
        
        if not node:
            return 0
        
        if not node.left and not node.right:
            self.max_path_sum = max(self.max_path_sum, node.val)
            return node.val
        
        l_path_sum = self.dfs(node.left)
        r_path_sum = self.dfs(node.right)
        
        self.max_path_sum = max(
        self.max_path_sum,
            node.val,
            node.val + l_path_sum,
            node.val + r_path_sum,
            node.val + l_path_sum + r_path_sum
        )
        
        return max(
        node.val,
        node.val + l_path_sum,
        node.val + r_path_sum,
        0)
        
        