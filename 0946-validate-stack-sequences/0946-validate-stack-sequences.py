class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        # two pointer technique
        # l on pushed and r on poped
        
        r = 0
        stack = []
        
        for l in pushed:
            stack.append(l)
            
            while stack and r < len(popped) and stack[-1] == popped[r]:
                r+=1
                stack.pop()
        return True if len(stack) == 0 else False
        
    