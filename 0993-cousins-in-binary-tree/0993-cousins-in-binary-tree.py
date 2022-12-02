# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        # Time complexity O(n)
        
        def dfs(node, parent, depth):
            if not node or len(results) == 2:
                return 
            else:
                if node.val == x or node.val == y:
                    results.append((parent, depth))
                dfs(node.left, node, depth+1)
                dfs(node.right, node, depth+1)
        
        results = []
        dfs(root, None, 0)

        return results[0][0] != results[1][0] and results[0][1] == results[1][1]
