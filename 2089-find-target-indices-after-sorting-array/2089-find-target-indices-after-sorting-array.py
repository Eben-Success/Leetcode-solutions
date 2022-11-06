class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        sortedNums = sorted(nums)
        list = []
        
        for i in range(0, len(sortedNums)):
            if sortedNums[i] == target:
                list.append(i)
            if target not in sortedNums:
                return
        return list
                
        
        
        