class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        
        # Edge cases
        if start == destination:
            return 0
        
        if start > destination:
            start, destination = destination, start
            
        clockWise = 0
        anticlockWise = 0
        
        for i in range(len(distance)):
            if i >= start and i < destination:
                clockWise += distance[i]
            else:
                anticlockWise += distance[i]
                
        return min(clockWise, anticlockWise)
        
        
        
        
        
        
        