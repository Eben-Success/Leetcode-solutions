class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        
        # Time: O(n)
        # Space: O(1)
        
        # Using Two pointers
        
#         l, r = 0, len(s) - 1
        
#         while l < r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
#         return s
        
        # Using Stack
        # Time: O(n)
        # Space: O(n)
        
        stack = []
        
        for char in s:
            stack.append(char)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
            
            
        
            
        