class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l, r = 0, 0
        
        l_word1 = list(word1)
        l_word2 = list(word2)
        
        res = []
        
        while l < len(word1) and r < len(word2):
            res.append(l_word1[l])
            l += 1
            res.append(l_word2[r])
            r += 1
            
        while l < len(word1):
            res.append(l_word1[l])
            l += 1

        while r < len(word2):
            res.append(l_word2[r])
            r += 1
            
        return "".join(res)
            
        