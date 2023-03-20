class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        res = []
        
        combined = list(zip(names, heights))
        
        combined.sort(key=lambda x:x[1], reverse=True)
        
        for name in combined:
            res.append(name[0])
        return res
        