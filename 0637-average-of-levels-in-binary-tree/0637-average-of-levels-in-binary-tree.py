# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res = []
        
        if not root:
            return res
        
        queue = deque([root])
        
        while queue:
            q_len = len(queue)
            level_order = 0
            
            for _ in range(q_len):
                node = queue.popleft()
                level_order += node.val
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            res.append(level_order / q_len)
            
        return res
        