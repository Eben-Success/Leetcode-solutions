class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # if (0, 0) or (-1, -1) is 1: return -1
        if grid[0][0] or grid[-1][-1]:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 1)])
        visited = set()
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        
        while q:
            r, c, path_len = q.popleft()
            
            # if the pop element is the last element, return path_len
            if (r, c) == (ROWS - 1, COLS - 1):
                return path_len
            
            for dr, dc in directions:
                n_row, n_col = dr + r, dc + c
                
                # create boundaries
                if (0 <= n_row < ROWS and 0 <= n_col < COLS and not grid[n_row][n_col]):
                    grid[n_row][n_col] = 1
                
                    q.append((n_row, n_col, path_len + 1))
        return -1
                    
        
            
        
        