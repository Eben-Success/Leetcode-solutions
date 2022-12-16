# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Time: O(n + m): root1 and root2
        # Space: O(n)
        
        # if no root1 or root2, return None
        if not root1 and not root2:
            return None
        
        # Get the vale of root1 and root2 if they exist, else 0
        val_1 = root1.val if root1 else 0
        val_2 = root2.val if root2 else 0
        
        root = TreeNode(val_1 + val_2)
        
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        
        return root
        
        
        
        
        
        
                
            
            
            
        
        