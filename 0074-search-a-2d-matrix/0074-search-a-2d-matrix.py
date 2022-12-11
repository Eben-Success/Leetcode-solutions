class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Brute force approach, you have to search the entire matrix to search for the target. 
        Time: O(m*n)
        
        We can use binary search to get O(mlogn)
        Apply 2 binary search, one for the row and the other for the 
        entire row.
        Time: O(logm + logn)
        """
        
        rows, cols = len(matrix), len(matrix[0])
        
        top, bottom = 0, rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            # if the target value is greater than the last element in 
            # the row
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
                
        if not (top <= bottom):
            return False
        
        l, r = 0, cols - 1
        row = (top + bottom) // 2
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
                
                
            