class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """Selection sort has space complexity of O(1)"""
        
        for step in range(len(nums)):
            min_idx = step
            
            for i in range(step+1, len(nums)):
                if nums[i] < nums[min_idx]:
                    min_idx = i
                    
            (nums[step], nums[min_idx]) = (nums[min_idx], nums[step])
        