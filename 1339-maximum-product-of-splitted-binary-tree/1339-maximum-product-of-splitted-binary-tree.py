# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree_sum = []
        
        def dfs(node):
            if not node:
                return 0
            
            l_sum = dfs(node.left)
            r_sum = dfs(node.right)
            
            cur_sum = l_sum + r_sum + node.val
            tree_sum.append(cur_sum)
            
            return cur_sum
            
        total_sum = dfs(root)
        max_product = 0
        
        for sum_ in tree_sum:
            max_product = max(max_product, sum_ * (total_sum - sum_))
            
        return max_product % (10**9 + 7)
            
        