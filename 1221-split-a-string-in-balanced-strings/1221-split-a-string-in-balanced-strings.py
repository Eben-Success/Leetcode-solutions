class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        # Time: O(n)
        # Space: O(1)
        
        count = {
            "L": 0,
            "R": 0
        }
        
        res = 0
        
        for char in s:
            count[char] += 1
            
            if count["L"] == count["R"]:
                res += 1
                
        return res


        
    
    
                
        