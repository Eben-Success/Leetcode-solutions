class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l = len(nums) - 1
        nums = sorted(nums)
        
        f = 0
       
        
        num_sum = 0
        max_num = 0
        
        while f < len(nums):
            num_sum = nums[f] + nums[l]
            max_num = max(num_sum, max_num)
            f += 1
            l -= 1
        return max_num
            
        
        
        
    
        
        