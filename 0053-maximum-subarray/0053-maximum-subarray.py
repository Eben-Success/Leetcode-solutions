class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # BRUTE FORCE APPROACH
        # Time: O(n^2)
        
        # res = float("-inf")
        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]
        #         res = max(res, cur_sum)
        # return res
        
        # OPTIMAL SOLUTION
        # Sliding Window | Time: O(n)
        
        max_sum = nums[0]
        cur_sum = 0
        
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
                
            cur_sum += n
            max_sum = max(max_sum, cur_sum)
        return max_sum
        
        