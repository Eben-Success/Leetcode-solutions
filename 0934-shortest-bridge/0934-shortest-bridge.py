class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        """
        Use bfs + dfs"""
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        visited = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROW or c == COL) or not grid[r][c] or (r, c) in visited:
                return 
            visited.add((r, c))
            
            for dr, dc in directions:
                dfs(dr + r, dc+ c)
                
        def bfs():
            queue = deque(visited)
            res = 0
            
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    
                    for dr, dc in directions:
                        n_row, n_col = r + dr, c + dc
                        
                        if (n_row < 0 or n_col < 0 or n_row == ROW or n_col == COL) or (n_row, n_col) in visited:
                            continue
                        if grid[n_row][n_col]:
                            return res
                        queue.append([n_row, n_col])
                        visited.add((n_row, n_col))
                res += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()
        