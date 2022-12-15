class Solution:
    def climbStairs(self, n: int) -> int:
    # Brute force: using decision tree wil yield a time of O(2^n)
    # Avoiding repeated task (using memoization) yields time of O(n)
    
    
    # Bottom Up Dynamic Programming Approah
    
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one