class Solution:
    def removeStars(self, s: str) -> str:
        # stack
        # append to stack
        # if star, stack.pop() until no star
        # continue
        
        # stack
        # loop through the characters in s and append it to the stack
        # check "*" in stack
        # if "*", stack.pop()
        # else stack.append()
    
        
        stack = []
      
        for i in range(len(s)):
            # while stack:
            if s[i] == "*":
                stack.pop()
            else: 
                stack.append(s[i])
                
        return "".join(stack)
        