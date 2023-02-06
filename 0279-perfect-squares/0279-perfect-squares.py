class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        
        squares = []
        
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
            
        queue = deque([(n, 0)])
        visited = set()
        
        while queue:
            num, level = queue.popleft()
            
            if num == 0:
                return level
            
            for square in squares:
                if num < square:
                    break
                    
                if (num - square, level+1) not in visited:
                    queue.append((num - square, level + 1))
                    visited.add((num - square, level + 1))
                    
        return -1
    
    
            
        