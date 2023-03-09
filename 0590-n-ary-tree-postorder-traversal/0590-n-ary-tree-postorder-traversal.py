"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res = []
        
        if not root:
            return res
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            stack.extend(node.children)
            
            res.insert(0, node.val)
            
        return res
        