class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        res = []
        
        hashmap = {}
        
        for num in nums:
            for i in range(len(num)):
                hashmap[num[i]] = 1 + hashmap.get(num[i], 0)
                
        for key, value in hashmap.items():
            if value == len(nums):
                res.append(key)
                
        return sorted(res)
                
        
            
        