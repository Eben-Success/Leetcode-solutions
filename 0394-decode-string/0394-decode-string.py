class Solution:
    def decodeString(self, s: str) -> str:
        
        
        # Time: O(n) | Space: O(n): stack
        
        stack = []
        
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                    
                stack.append(int(k) * substr)
                
        return "".join(stack)