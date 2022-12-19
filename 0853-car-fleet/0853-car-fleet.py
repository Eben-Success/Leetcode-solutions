class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Time: O(nlogn): sort the array of the position
        # Space: O(n): stack
        
        # merge the position and speed
        pair = [[p, s] for p, s in zip(position, speed)]
        
        stack = []
        
        # sorted pair in descending order
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            
            # check if len(stack) >= 2
            # check if current speed <= previous speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)
            