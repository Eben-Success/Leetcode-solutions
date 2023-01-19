from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [i for i in range(n)]
        
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        leaves = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
                
        while n > 2:
            size = len(leaves)
            n -= size
            
            for _ in range(size):
                u = leaves.popleft()
                v = adj[u].pop()
                adj[v].remove(u)
                
                if len(adj[v]) == 1:
                    leaves.append(v)
                    
        return list(leaves)