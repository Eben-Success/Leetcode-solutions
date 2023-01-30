class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        visited = [False] * n
        count = 0
        
        for i in range(n):
            if not visited[i]:
                count += 1
                self.dfs(isConnected, visited, i)
        return count
    
    
    def dfs(self, isConnected, visited, city):
        n = len(isConnected)
        visited[city] = True
        
        for i in range(n):
            if isConnected[city][i] and not visited[i]:
                self.dfs(isConnected, visited, i)