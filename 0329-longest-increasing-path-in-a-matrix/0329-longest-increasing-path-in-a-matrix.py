class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.memo = {}
        res = 1
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, self.dfs(matrix, r, c))
        return res
    
    
    def dfs(self, matrix, r, c):
        if (r, c) in self.memo:
            return self.memo[(r, c)]
        
        self.memo[(r, c)] = 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row_inc, col_inc in directions:
            new_row = row_inc + r
            new_col = col_inc + c
            
            if (0 <= new_row < len(matrix)) and (0 <= new_col < len(matrix[0])) and matrix[r][c] < matrix[new_row][new_col]:
                self.memo[(r, c)] = max(self.memo[(r,c)], 1 + self.dfs(matrix, new_row, new_col))
                
        return self.memo[(r, c)]
        
        