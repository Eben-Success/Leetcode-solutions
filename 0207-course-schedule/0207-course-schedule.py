class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create an adjacency list to represent the graph of courses
        graph = [[] for _ in range(numCourses)]
        
        # create an array to store the number of incoming edges for each node
        indegree = [0] * numCourses
        
        # Fill the adjacency list and indegree array based on the input prerequisites
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        # Create a queue to store the nodes (courses) with no incoming edges
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        # Traverse the graph starting from the nodes (courses) with no incoming edges
        
        while queue:
            course = queue.popleft()
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return sum(indegree) == 0
        