class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        hashmap = {}
        
        for stone in stones:
            hashmap[stone] = 1 + hashmap.get(stone, 0)
            
        count = 0
        for key, value in hashmap.items():
            if key in jewels:
                count += value
                
        return count
                
            
            
        