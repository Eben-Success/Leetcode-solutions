class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        
        start = 0
        end = 0
        max_len = 0
        dic = {}
        
        while end < len(fruits):
            dic[fruits[end]] = end
            if len(dic) >= 3:
                min_val = min(dic.values())
                del dic[fruits[min_val]]
                start = min_val + 1
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
        