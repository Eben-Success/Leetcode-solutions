class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # Time: O(logn)
        
        if n <= 0: return False
        
        res = round(log(n, 3))
        return 3** res == n
        