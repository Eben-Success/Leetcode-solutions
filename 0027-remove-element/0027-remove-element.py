class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        count = 0
        for i in range(n):
            if nums[i] != val:
                nums[count] = nums[i]
                count +=1
        return count
                
            
        