class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Space complexity is O(n)
        # Time complexity is O(n)
        
        charSet = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res