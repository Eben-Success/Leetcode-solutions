class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        """
        1. Alice: left to right
        Bob: right to left
        
        2. More capacity waters.
        
        3. same capactiy: Alice waters
        """
        
        n = len(plants)
        waterA, waterB = capacityA, capacityB
        refill = 0
        l, r = 0, n - 1
        
        while l < r:
            
            if waterA < plants[l]:
                waterA = capacityA
                refill += 1
            waterA -= plants[l]
            l += 1
            
            if waterB < plants[r]:
                waterB = capacityB
                refill += 1
            waterB -= plants[r]
            r -= 1
            
        if l == r and waterA < plants[l] and waterB < plants[r]:
            refill += 1
        return refill
                
            