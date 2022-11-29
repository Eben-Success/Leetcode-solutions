class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * (len(temperatures))
        stack = [] # pair: [temp, index]
        
        for idx, temp in enumerate(temperatures):
            # while stack is not empty and the last element on our stack
            # is < temp
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = (idx - stackIdx)
            stack.append([temp, idx])
        return res
        
       
            
            
            
            
        