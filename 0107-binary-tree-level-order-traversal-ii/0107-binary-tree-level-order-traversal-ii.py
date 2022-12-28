# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            level_items = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                level_items.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            res.append(level_items)
        return res[::-1]
        