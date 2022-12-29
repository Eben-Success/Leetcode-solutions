class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums.sort()
        res = 0
        l = 0
        
        for r in range(1, len(nums)):
            if nums[r] <= nums[l]:
                res += nums[l] - nums[r] + 1
                nums[r] = nums[l] + 1
            l = r
        return res
                
        
        
        