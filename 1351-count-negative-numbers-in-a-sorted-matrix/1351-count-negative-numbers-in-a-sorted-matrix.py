class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        """
        [[4,3,2,-1]
        [3,2,1,-1]
        [1,1,-1,-2]
        [-1,-1,-2,-3]]"""
        
        count = 0
        for row in grid:
            for col in row:
                if col < 0:
                    count += 1
                    
        return count
        