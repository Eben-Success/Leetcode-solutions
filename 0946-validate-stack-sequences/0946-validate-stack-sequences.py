class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        # two pointer technique
        # l on pushed and r on popped
        
        r = 0
        stack = []
        
        for l in range(len(pushed)):
            stack.append(pushed[l])
            
            while stack and r < len(popped) and stack[-1] == popped[r]:
                stack.pop()
                r+=1
        return stack == []
        
        
    