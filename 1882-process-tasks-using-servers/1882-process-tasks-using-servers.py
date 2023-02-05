class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        # Time: O(nlogm)
        # Space: O(n)
        
       
        # two main heaps, one for available server, one for unavailable.
        # available = (weight, index)
        # unavailable = (timeServerBecomesFree, weight, index)

        
        res = [0] * len(tasks)
    
        available = [(servers[i], i) for i in range(len(servers))]

        heapq.heapify(available)

        unavail = []

        t = 0

        for i in range(len(tasks)):
            t = max(t, i)

            if len(available) == 0:
                t = unavail[0][0]

            while unavail and t >= unavail[0][0]:
                timefree, weight, index = heapq.heappop(unavail)

                heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            res[i] = index

            heapq.heappush(unavail, (t + tasks[i], weight, index))

        return res
    
    
#         #BRUTE FORCE APPROACH
#         # Time: O(m * n)
#         # Space: O(n)
#         n = len(servers)
#         m = len(tasks)
        
#         servers = [(server, i) for i, server in enumerate(servers)]
#         servers.sort()
#         ans = [0] * m
#         q = PriorityQueue()
#         time = 0
        
#         for i in range(m):
#             while servers and servers[0][0] <= time:
#                 _, j = servers.pop(0)
                
#                 q.put(j)
#             if q.empty():
#                 time = servers[0][0]
                
#             j = q.get()
#             ans[i] = j
#             time += tasks[i]
#             q.put(j)
#         return ans


        
