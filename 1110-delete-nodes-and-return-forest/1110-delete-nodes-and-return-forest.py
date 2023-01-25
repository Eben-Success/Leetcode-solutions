# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        self.forest = []
        self.dfs(root, to_delete, True)
        return self.forest
        
    def dfs(self, node, to_delete, is_root):
        if not node:
            return
        
        if node.val in to_delete:
            self.dfs(node.left, to_delete, True)
            self.dfs(node.right, to_delete, True)
            
        else:
            if node.left:
                if node.left.val in to_delete:
                    self.dfs(node.left, to_delete, True)
                    node.left = None
                else:
                    self.dfs(node.left, to_delete, False)
            
            if node.right:
                if node.right.val in to_delete:
                    self.dfs(node.right, to_delete, True)
                    node.right = None
                    
                else:
                    self.dfs(node.right, to_delete, False)
                
            if is_root:
                self.forest.append(node)

        