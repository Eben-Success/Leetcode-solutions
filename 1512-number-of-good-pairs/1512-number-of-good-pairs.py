class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        """
        Use two pointers
        If the indexes of two pointers are same, add 1 to count
        """
        
        # Naive Approach
        # Time: O(n^2)
        # Space: O(1)
        
#         count = 0
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1         
#         return count
    
        # Time: O(n)
        # Space: O(n)
        
        hashmap = {}
        
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
            
        good_pairs = 0
        for key in hashmap:
            n = hashmap[key]
            
            good_pairs += n*(n-1)//2
            
        return good_pairs
            
        
        
        