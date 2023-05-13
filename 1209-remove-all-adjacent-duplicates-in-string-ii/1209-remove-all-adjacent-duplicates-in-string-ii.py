class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        if len(s) == 0:
            return s

        stack = []
        
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
                
            else:
                stack[-1][1] += 1
                
            
            if stack[-1][1] == k:
                stack.pop()
                
        res = ""
        
        for char, count in stack:
            res += char * count
            
        return res
                
        
            
            
            
        
        
                    
                