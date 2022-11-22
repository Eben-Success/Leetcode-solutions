import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        dic = {}
        
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
                
        for key, val in dic.items():
            if len(res) < k:
                heapq.heappush(res, [val, key])
            else:
                heapq.heappushpop(res, [val, key])
        return [key for value, key in res]
        