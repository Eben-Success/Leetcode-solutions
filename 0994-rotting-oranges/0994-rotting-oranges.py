class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time: O(m*n): m & n are dimensions of the grid
        # Space: O(m*n)
        
        """
        TODO
        1. Use breadth first traversal
        2. Initialize time and fresh oranges
        3. 
        """
        
        q = deque([])
        fresh, time = 0, 0
        
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r, c])
                    
        directions= [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    # if in bounds and fresh
                    if (row < 0 or row == ROWS or 
                        col < 0 or col == COLS or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
                
        return time if fresh == 0 else -1
                    
                    
                        

                    
                    
        
        