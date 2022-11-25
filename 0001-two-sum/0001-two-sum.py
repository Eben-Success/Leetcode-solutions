class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Time complexity of O(n)
        # Space Complexity of O(n)
        
        HashMap = {} # val: index
        
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in HashMap:
                return [HashMap[diff], idx]
            HashMap[num] = idx
        
        
       
        
        