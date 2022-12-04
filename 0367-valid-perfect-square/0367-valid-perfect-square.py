class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search
        # Time complexity O(logn)
        # Space complexity O(1)
        
        
        low = 0
        high = num
        
        while low <= high:
            mid = (low + high) // 2
            
            if (mid*mid) == num:
                return True
            elif (mid*mid) < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
        