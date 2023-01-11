from heapq import heapify, heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

#         nums = [-x for x in nums]
#         heapify(nums)

#         while nums:
#             cur = heappop(nums)
#             k -= 1
#             if k == 0:
#                 return - (cur)
            
        nums = [-x for x in nums]
        
        heapify(nums)
        
        while nums and k > 0:
            cur = heappop(nums)
            k -= 1
        return - cur