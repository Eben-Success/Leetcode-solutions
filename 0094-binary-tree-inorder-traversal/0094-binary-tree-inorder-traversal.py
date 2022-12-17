# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Traverse left, root, and right
        
        # Time: O(n)
        # Space: O(n): call stack
        
        res = []
        
        def inorder(root):
            if root is None:
                return
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return res
    
    
    
        # Iterative Solution
        # Time: O(n)
        # Space: O(n + m): stack and res
        
#         res = []
#         stack = []
#         cur = root
        
#         while stack or cur:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             res.append(cur.val)
#             cur = cur.right
#         return res
                
        