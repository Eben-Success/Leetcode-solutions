class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Brute force Approach
        # Time: O(n^3): the two for loops and computing the sum
        # Space: O(1)
        
        # count = 0
        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]
        #         if cur_sum == k:
        #             count += 1
        # return count
        
        # Using Prefix sum and Hashmap
        # Time: O(n) | Space: O(n)
        
        res = 0
        cur_sum = 0
        prefix_sum = {0 : 1}
        
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            
            res += prefix_sum.get(diff, 0)
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
            
        return res
        
        
        
        
        