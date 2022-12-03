class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        Maxdq, Mindq = deque(), deque()
        res = 0
        l = 0
        n = len(nums)
        
        for r in range(n):
            while Maxdq and nums[Maxdq[-1]] < nums[r]:
                Maxdq.pop()
            while Mindq and nums[Mindq[-1]] >= nums[r]:
                Mindq.pop()
            Maxdq.append(r)
            Mindq.append(r)
            
            while nums[Maxdq[0]] - nums[Mindq[0]] > limit:
                l += 1
                if Maxdq[0] < l: Maxdq.popleft()
                if Mindq[0] < l: Mindq.popleft()
            res = max(res, r - l + 1)
        return res
        