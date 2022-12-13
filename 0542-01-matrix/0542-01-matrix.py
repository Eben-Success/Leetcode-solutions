class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(mat), len(mat[0])
        q = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c))
                
                else:
                    mat[r][c] = "#"
                    
        for row, column in q:
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nr = row + dx
                nc = column + dy
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] == "#":
                    mat[nr][nc] = mat[row][column] + 1
                    q.append((nr, nc))
        return mat
                    
        