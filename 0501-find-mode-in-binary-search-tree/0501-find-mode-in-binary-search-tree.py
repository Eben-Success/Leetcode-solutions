# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        
        
        
        freqs = {}
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            freqs[cur.val] = 1 + freqs.get(cur.val, 0)
            cur = cur.right
            
            
        # Find the modes from the max_frequencies
        
        max_freqs = max(freqs.values())
        
        modes = [val for val, freq in freqs.items() if freq == max_freqs]
        
        return modes