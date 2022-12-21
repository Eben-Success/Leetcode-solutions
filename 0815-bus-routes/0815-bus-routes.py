class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        # Check Note
        # BFS
        
        # Edge case
        if source == target:
            return 0
        
        # create adjacency list 
        graph = collections.defaultdict(set)
        
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
                
        # use set to prevent infinite loops
        visited_buses = set()
        visited_stop = set()
        
        q = collections.deque([(source, 0)])
        
        while q:
            stop, route_len = q.popleft()
            
            if stop == target:
                return route_len
            
            # routes the bus can take
            for bus in graph[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    
                    # stops the bus can reach
                    for stop in routes[bus]:
                        if stop not in visited_stop:
                            visited_stop.add(stop)
                            
                            q.append((stop, route_len + 1))
                            
        return -1
                            
                            
                        
                    
        
        
        
        