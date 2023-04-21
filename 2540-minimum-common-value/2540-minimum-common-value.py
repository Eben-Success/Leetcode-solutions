class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        Since the arrays are sorted,
        using two pointers is the ideal solution.
        """
        
        l, r = 0, 0
        
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
                
            else:
                # nums1[l] == nums[r]:
                return nums1[l]
            
        return -1
            