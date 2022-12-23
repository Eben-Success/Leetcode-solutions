class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        # Edge
        if k >= (ROWS - 1) + (COLS - 1):
            return (ROWS - 1) + (COLS - 1)
        
        # define target
        target = (ROWS - 1, COLS - 1)
        
        # Using Breadth First Search
        queue = collections.deque([(0, (0, 0, k))])
        seen = set([(0, 0, k)])
        
        # while the queue is not empty
        while queue:
            cur_path, (row, col, k_left)= queue.popleft()
            
            # if current position is equal to target: return current path
            if (row, col) == target:
                return cur_path
            
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            
            # traverse grid 4 directionally using directions above
            for row_inc, col_inc in directions:
                n_row = row_inc + row
                n_col = col_inc + col
                
                # Keep traversal inbound
                if (0 <= n_row < ROWS) and (0 <= n_col < COLS):
                    new_k = k_left - grid[n_row][n_col]
                    new_state = (n_row, n_col, new_k)
                    
                    # check if some k still remains and new state is not in seen set
                    if new_k >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((cur_path + 1, new_state))
                    
        return -1
                    
            
        