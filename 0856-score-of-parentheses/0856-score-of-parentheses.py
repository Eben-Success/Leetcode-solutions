class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        # time complexity O(1)
        # space complexity = O(n)
        
        """Use Stack to implement our solution.
        if open parenthesis, add score to stack, else pop from stack
        and add to the max of score * 2 and 1"""
        
        stack = []
        score = 0
        
        for c in list(s):
            if c == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score*2, 1)
        return score
    
    