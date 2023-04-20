class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        prefix = ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for word in strs[1:]:
                if i >= len(word) or char != word[i]:
                    return prefix
            prefix += char
                
        return prefix
                    
        