class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Sliding window
        # Time: O(n)
        
        # Edge case
        if len(s1) > len(s2):
            return False
        
        s1_count = self.create_character_count_map(s1)
        
        for i in range(len(s2) - len(s1) + 1):
            s2_count = self.create_character_count_map(s2[i:i+len(s1)])
            if s2_count == s1_count:
                return True
    
    def create_character_count_map(self, s):
        count_map = {}
        
        for c in s:
            if c in count_map:
                count_map[c] += 1
            else:
                count_map[c] = 1
                
        return count_map