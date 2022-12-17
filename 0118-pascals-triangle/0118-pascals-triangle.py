class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # Time: O(n**2): n rows with n operations
        # Space: O(n**2)
        
        
        res= [[1]]
        
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            newRow = []
            
            for j in range(len(res[-1]) + 1):
                newRow.append(temp[j] + temp[j+1])
            res.append(newRow)
        return res