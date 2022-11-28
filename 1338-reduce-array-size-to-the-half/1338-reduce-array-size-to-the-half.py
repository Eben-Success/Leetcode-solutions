class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Use counter to store the occurances of the array in dictionary
        # sorted the dictionary in descending order.
        # check if the n >= half of the array
        
        c = Counter(arr)
        N = len(arr)
        count = 0
        n = 0
        
        # sorts the dictionary in descending order
        for k, v in sorted(c.items(), key=lambda x: -x[1]):
            n += v
            count += 1
            
            if n >= (N//2): break
        return count
            
        
        
        
        
        
            
        