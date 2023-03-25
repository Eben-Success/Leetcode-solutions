# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
#         if not root:
#             return 0
        
#         if not root.left and not root.right:
#             return 1
        
#         left_depth = self.minDepth(root.left)
#         right_depth = self.minDepth(root.right)
        
#         if left_depth == 0 or right_depth == 0:
#             return max(left_depth, right_depth) + 1
        
#         return min(left_depth, right_depth) + 1
    
    
    # Iterative approach
    
    # using breadth first search
    
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            if node.left is None and node.right is None:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
                
            if node.right:
                queue.append((node.right, depth + 1))
                