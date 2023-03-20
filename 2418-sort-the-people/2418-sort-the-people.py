class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        # zip names and height into a List
        combined = list(zip(names, heights))
        
        # sort the list by the second index
        combined.sort(key=lambda x:x[1], reverse=True)
        
        # Append the first index sorted_names
    
        sorted_names = [x[0] for x in combined]
        
        return sorted_names
    
        
        