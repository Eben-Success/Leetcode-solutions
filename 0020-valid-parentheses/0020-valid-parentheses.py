class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        # Check if closing parenthesis is in Hashmap
        
        for c in s:
            if c in closeToOpen:
                
                # Check for stack and the last element in stack to see if it matches with opening parenthesis.
                if stack and stack[-1] == closeToOpen[c]:
                    
                    # if True, remove opening and closing parenthesis from stack.
                    stack.pop()
                else: 
                # Else return False
                    return False
            
            # If closing parenthesis not in stack, add it to stack
            else: 
                stack.append(c)
        # Return true if stack is empty or False is not.
        return True if not stack else False
            