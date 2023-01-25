class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # create adjacency list
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            
        # create an indegree array
        indegree = [0 for _ in range(numCourses)]
        for prereq in adj_list:
            for course in adj_list[prereq]:
                indegree[course] += 1
         
        # create a queue and add all vertices with indegree of 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        # create a result list
        res = []
        
        # perform topological sorting
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
            for nei in adj_list[vertex]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        if len(res) < numCourses:
            return []
        return res