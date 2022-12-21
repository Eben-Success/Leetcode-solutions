class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # DFS
        
        # m: # of accounts | n: max number of email per person
        # Time: O(m*n) * mlogk
        # Space: O(m*n)
        
        graph = defaultdict(set)
        # a map that takes email and maps to name
        email_to_name = {}
        
        # Get the name from each list
        for account in accounts:
            name = account[0]
            
            # create adjacency list for names & emails
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                
                email_to_name[email] = name
                
        res = []
        visited = set()
        
        # traverse the graph, and process each current email
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                
                local_res = []
                
                # while the stack is not empty, process the cur_email on the stack
                while stack:
                    cur_email = stack.pop()
                    local_res.append(cur_email)
                    
                    # Process the neighbors of cur_email
                    for nei in graph[cur_email]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)
                            
                res.append([email_to_name[email]] + sorted(local_res))
                
        return res
                            
                            
                        
            
        
                
                
            
            
        
        