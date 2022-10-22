class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, mid = 0, 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                low = mid + 1
            
            else:
                high = mid - 1
                
        return low
                
        