# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        if not k:
            return [target.val]
        
        # a graph to create adjacency list
        graph = collections.defaultdict(list)
        
        # a queue to process the nodes
        queue = collections.deque([root])
        
        # Process the nodes from the queue while the it is not empty
        while queue:
            node = queue.popleft()
            
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                
                queue.append(node.left)
                
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                
                queue.append(node.right)
                
                
        # Breadth First Search
        res = []
        queue = collections.deque([(target, 0)])
        visited = set([target])
        
        # process queue while it is not empty
        while queue:
            node, distance  = queue.popleft()
            
            if distance == k:
                res.append(node.val)
            else:
                # process the neighbors of node
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append([edge, distance + 1])
                        
        return res
            
        
        