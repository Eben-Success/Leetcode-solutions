class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        # Time: O(nlogn)
        # Space: O(n): queue
        
        res, queue = deque(), deque()
        
        changed.sort()
        
        for num in changed:
            if queue and num == queue[0] * 2:
                res.append(queue.popleft())
                
            else:
                queue.append(num)
                
        return [] if queue else res
        