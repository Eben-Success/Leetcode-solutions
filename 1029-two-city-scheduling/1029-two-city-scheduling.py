class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        """
        
        Clarification:
        1. Is the length of the array even?
        2. 2 * len(cost) is the actual length of the costs?
        
        
        Sending each person to city A, yield a totalcost of 
        10 + 30 + 400 + 30 = 470 
        
        Now, since we have already paid for tickets to city A, 
        we need to deduct the cost of traveling to city B from A to 
        check who get more refund. -ve means refund | +ve means pay more.
        
        
        refund[i] = cost[i][1] - cost[i][0]
        That yeilds = 10, 170, -350, -10
        
        We sort the refund =[-350, -10, 10, 170]
        
        Get refund for -ve => 470 - 350 - 10 => 110
        """
        
        n = len(costs) // 2
        
        refund = []
        min_cost = 0
        
        for a_cost, b_cost in costs:
            refund.append(b_cost - a_cost)
            min_cost += a_cost
            
        refund.sort()
        
        for i in range(n):
            min_cost += refund[i]
            
            
        return min_cost
        
        
            
        