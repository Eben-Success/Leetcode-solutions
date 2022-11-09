class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        srt = sorted(nums)
        
        l = 0
        r = len(srt) - 1
        count = 0
        
        while l < r:
            if srt[l] + srt[r] == k:
                count += 1
                l += 1
                r -= 1
                
            elif srt[l] + srt[r] < k:
                l += 1
            elif srt[l] + srt[r] > k:
                r -= 1
        return count
        