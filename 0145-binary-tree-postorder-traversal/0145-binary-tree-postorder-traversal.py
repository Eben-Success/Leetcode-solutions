# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         res = []
        
#         if root:
#             res += self.postorderTraversal(root.left)
#             res += self.postorderTraversal(root.right)
#             res.append(root.val)
#         return res


#           Second solution

#         if not root:
#         return []
    
#         left = self.postorderTraversal(root.left)
#         right = self.postorderTraversal(root.right)
        
#         return left + right + [root.val]
        
        
        # Iterative Approach
        # Post order traversal is a reverse of inorderTraversal
        
        if not root:
            return []
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
            res.insert(0, node.val)
        return res
        
            