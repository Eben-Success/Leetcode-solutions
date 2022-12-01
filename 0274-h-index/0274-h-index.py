class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # find the max(integer that is greater or eqaul to itself in order integers.)
        
        # Time complexity of (nlogn)
        
        citations.sort(reverse=True)
        
        for idx, citation in enumerate(citations):
            if idx >= citation:
                return idx
        return len(citations)
            
            
        
        
            
        