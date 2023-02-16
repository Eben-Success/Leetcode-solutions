class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        mp, res = {}, 0
        
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                diff = target - (arr[i] + arr[j])
                res += mp[diff] if diff in mp else 0
                
            # mp[arr[i]] = mp.get(arr[i], 0) + 1
            
            if arr[i] in mp: mp[arr[i]] += 1
            else: mp[arr[i]] = 1
            
        return res % int(1e9 + 7)
        