class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip all special characters.
        # convert to lower case
        
        newStr = []
        
        for c in s:
            if c.isalnum():
                newStr.append(c.lower())
        # take new string and compare with reverse Str
        return True if newStr == newStr[::-1] else False
        
        
        