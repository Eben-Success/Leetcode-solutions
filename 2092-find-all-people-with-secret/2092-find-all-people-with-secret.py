class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        meetings.sort(key=lambda x: x[2])
        
        meeting_dict = collections.defaultdict(list)
        
        for person1, person2, time in meetings:
            meeting_dict[time].append([person1, person2])
            
        has_secret = {0, firstPerson}
        
        for time, meetings in meeting_dict.items():
            graph = collections.defaultdict(list)
            
            seen = set()
            
            for person1, person2 in meetings:
                graph[person1].append(person2)
                graph[person2].append(person1)
                
                if person1 in has_secret:
                    seen.add(person1)
                    
                if person2 in has_secret:
                    seen.add(person2)
                    
            queue = collections.deque(seen)
            
            while queue:
                person = queue.popleft()
                
                for neighbor in graph[person]:
                    if neighbor not in has_secret:
                        has_secret.add(neighbor)
                        queue.append(neighbor)
                        
        return has_secret
        