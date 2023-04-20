class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hashmap = {}
        
        for char in ransomNote:
            hashmap[char] = 1 + hashmap.get(char, 0)
            
        for char in magazine:
            if char in hashmap:
                hashmap[char] -= 1
                
        return all(num <= 0 for num in hashmap.values())
        