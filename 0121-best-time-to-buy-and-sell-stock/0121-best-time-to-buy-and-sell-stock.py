class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointers
        # l , r 
        # Profit between the two pointers.
        # maxProfit = 0
        
        # Time complexity of O(n)
        # Space complexity of O(1)
        
        l = 0
        maxProfit = 0
        
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
        return maxProfit
            