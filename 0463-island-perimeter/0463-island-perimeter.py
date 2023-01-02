class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # to avoid infinity loops
        visited = set()
        
        # define a dfs (nested function)
        def dfs(r, c):
            # Edge case
            
            # check for boundaries and water
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0:
                return 1
            
            # check for visited
            if (r, c) in visited:
                return 0
            visited.add((r,c))
            
            # Run dfs to calculate the perimeter
            
            perimeter = dfs(r, c -1)
            perimeter += dfs(r, c+1)
            perimeter += dfs(r-1, c)
            perimeter += dfs(r+1, c)
            return perimeter
        
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return dfs(r, c)
        
        