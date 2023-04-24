class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        universal = list(range(1, 2001))
        
        missing = list(set(universal) - set(arr))
        
        heapq.heapify(missing)
        
        while k > 0 and missing:
            kth = heapq.heappop(missing)
            k -= 1
            
        return kth
                
        