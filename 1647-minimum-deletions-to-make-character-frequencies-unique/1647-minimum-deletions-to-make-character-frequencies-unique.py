class Solution:
    def minDeletions(self, s: str) -> int:
        
        # Time: O(n) + O(n) -> O(n)
        # Space: O(26) + O(n) -> O(n): for 26 alphabet in the Counter(s)
        
        char_count = collections.Counter(s)
        deletion = 0
        
        freq_set = set()
        
        for char, count in char_count.items():
            while count > 0 and count in freq_set:
                count -= 1
                
                deletion += 1
                
            freq_set.add(count)
            
        return deletion
        
        
        
    