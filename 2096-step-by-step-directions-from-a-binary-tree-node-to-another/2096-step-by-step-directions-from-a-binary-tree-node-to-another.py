# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # Time: O(n)
        # Space: O(n)
        
        # convert binary tree into adjacency list using graph
        graph = collections.defaultdict(list)
        
        # use queue to process the root and convert into the adjacency list
        queue = collections.deque([root])
        
        # while the queue is not empty
        while queue:
            node = queue.popleft()
            
            if node.left:
                graph[node.left.val].append((node.val, "U"))
                graph[node.val].append((node.left.val, "L"))
                
                queue.append(node.left)
                
            if node.right:
                graph[node.right.val].append((node.val, "U"))
                graph[node.val].append((node.right.val, "R"))
                
                queue.append(node.right)
                
        # Breadth first search
                
        queue = collections.deque([(startValue, "")])
        visited = set()
        
        while queue:
            cur_val, cur_path = queue.popleft()
            
            if cur_val in visited:
                continue
                
            visited.add(cur_val)
            
            if cur_val == destValue:
                return cur_path
            else:
                for nei, direction in graph[cur_val]:
                    queue.append((nei, cur_path + direction))
            
        