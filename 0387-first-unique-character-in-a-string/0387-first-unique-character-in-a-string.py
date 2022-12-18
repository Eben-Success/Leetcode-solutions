class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = {}
        
        for char in s:
            count[char] = 1 + count.get(char, 0)
            
        for idx in range(len(s)):
            if count[s[idx]] == 1:
                return idx
        return -1