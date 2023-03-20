class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        res = []
        
        # zip names and height into a List
        combined = list(zip(names, heights))
        
        # sort the list by the second index
        combined.sort(key=lambda x:x[1], reverse=True)
        
        # Append the first index to res and return it
        for name in combined:
            res.append(name[0])
        return res
        