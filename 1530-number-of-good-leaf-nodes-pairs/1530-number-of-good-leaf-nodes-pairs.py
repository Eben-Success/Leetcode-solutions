# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        # Dpeth first search to return the lenght of each btn leafs
        
        # Edge case
        if not root:
            return 0
        
        self.good_pairs = 0
        
        self.postorder(root, distance)
        return self.good_pairs
    
    def postorder(self, node, distance):
        if not node:
            return []
        
        if not node.left and not node.right:
            return [1]
        
        left_distances = self.postorder(node.left, distance)
        right_distances = self.postorder(node.right, distance)
        
        for left_distance in left_distances:
            if left_distance >= distance:
                continue
                
            for right_distance in right_distances:
                self.good_pairs += 1 if left_distance + right_distance <= distance else 0
                
        return [1 + dist for dist in left_distances + right_distances]
        
        
        
        
        