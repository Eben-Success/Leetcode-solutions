class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
#         visited = set()
#         queue = deque([source])
#         graph = self.build_graph(edges)
        
#         while len(queue) > 0:
#             current = queue.popleft()
#             if current == destination:
#                 return True
            
#             for neighbor in graph[current]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#                 visited.add(neighbor)
#         return False
    
        
        
#     def build_graph(self, edges):
#         graph = {}
#         for edge in edges:
#             a, b = edge
#             if a not in graph:
#                 graph[a] = []
#             if b not in graph:
#                 graph[b] = []
#             graph[a].append(b)
#             graph[b].append(a)
#         return graph


        graph = defaultdict(list)
        queue = deque()
        
        # create adjacency list
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        # begin breadth first search
        # initialize visited and source in queue
        
        queue.append(source)
        visited = set()
        
        while queue:
            currentNode = queue.popleft()
            if currentNode == destination:
                return True
            visited.add(currentNode)
            
            for neighbor in graph[currentNode]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        