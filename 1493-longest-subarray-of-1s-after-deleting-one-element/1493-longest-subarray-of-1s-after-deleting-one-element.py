class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        res = 0
        k = 1 # max number of zeros we can delete
        l = 0
        
        for r in range(len(nums)):
            # if we encounter a zero, decrement
            # the num zeros we can now delete
            if nums[r] == 0:
                k -= 1
                
            # if we've seen more than one zero
            # move the left pointer until we
            # have discarded the first zero
            # we have encountered hence making the 
            # sliding window (l..r) valid again
                
            while k < 0 and l <= r:
                if nums[l] == 0:
                    k += 1
                l += 1
                
            # make sure you're not adding +1
            # to the sliding window because we
            # want to also account for the deleted
            #zero, so don't index correct here
            res = max(res, r - l)
        return res
        