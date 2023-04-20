class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return len(nums)
        
        pos = 2
        
        for i in range(2, len(nums)):
            if nums[i] != nums[pos - 2]:
                nums[pos] = nums[i]
                pos += 1
                
        return pos
        