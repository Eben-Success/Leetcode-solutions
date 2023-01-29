class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        
        while heap:
            val, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            
            if i == m - 1 and j == n - 1:
                return val
            
            if i + 1 < m:
                heapq.heappush(heap, (val + grid[i+1][j], i + 1, j))
                
            if j + 1 < n:
                heapq.heappush(heap, (val + grid[i][j+1], i, j+1))
                
        return 0
        