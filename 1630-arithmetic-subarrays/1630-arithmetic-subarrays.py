class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        m = len(l)
        result = []
        for i in range(m):
            subarray = nums[l[i]:r[i]+1]
            subarray.sort()
            if len(subarray) < 3:
                result.append(True)
            else:
                common_difference = subarray[1] - subarray[0]
                is_arithmetic = True
                for j in range(1, len(subarray)):
                    if subarray[j] - subarray[j-1] != common_difference:
                        is_arithmetic = False
                        break
                result.append(is_arithmetic)
        return result
        