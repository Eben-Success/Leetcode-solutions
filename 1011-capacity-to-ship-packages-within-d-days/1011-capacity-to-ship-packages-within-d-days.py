class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            if self.can_ship(mid, weights, days):
                right = mid
                
            else:
                left = mid + 1
                
        return right
    
    
    def can_ship(self, candidate, weights, days):
        days_taken = 1
        cur_weight = 0
        
        for weight in weights:
            cur_weight += weight
            
            if cur_weight > candidate:
                days_taken += 1
                cur_weight = weight
                
        return days_taken <= days