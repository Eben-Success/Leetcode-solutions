class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        string = ""
        res = 0
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            string += str(nums[l])
            l += 1
            string += str(nums[r])
            r -= 1
            
            res += int(string)
            string = ""
            
        if l == r: # if there's only one element left
            res += nums[l]
        
        return res