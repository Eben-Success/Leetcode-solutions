class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Time: O(nlogn): sort the array of the position
        # Space: O(n): stack
        
        pair = [[p, s] for p, s in zip(position, speed)] # list comprehension
        
        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order
            stack.append((target - p) / s)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)