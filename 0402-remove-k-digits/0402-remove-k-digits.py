class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Using monotonic stack
        # Time complexity is O(n)
        # Space complexity is O(1)
        
        # check if the cur < stack[-1]: append it else pop from stack
        
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k-=1
                stack.pop()
            stack.append(c)
            
        stack = stack[:len(stack) -k]
        res = "".join(stack)
        return str(int(res)) if res else "0"
     
                
        
        
        
        
        