class Solution:
    def isPalindrome(self, s: str) -> bool:
          # strip all special characters.
        # convert to lower case
        
        # LIMITATIONS
        #Space is O(n) and involves special function
        
#         newStr = []
        
#         for c in s:
#             if c.isalnum():
#                 newStr.append(c.lower())
#         # take new string and compare with reverse Str
#         return True if newStr == newStr[::-1] else False

        
        # SECOND SOLUTION
        
        # Using two pointers
        
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True 
            
        # ord deals with strings
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') 
                or ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
        