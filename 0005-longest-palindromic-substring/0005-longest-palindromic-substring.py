class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # take each character and expand outwards.
        
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # check odd length palindrome
            l,r = i, i # l & r initially points to the center position.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # checking even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
            
            
            
        
        
        