class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        
        while low + 1 < high:
            mid = (low +high) // 2
            
            if (mid * mid) == x:
                return mid
            
            elif (mid * mid) < x:
                low = mid
            else:
                high = mid
        if (high * high) == x:
            return high
        return low
      
        