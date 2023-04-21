class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = set()
        
        nums1.sort()
        nums2.sort()
        
        l, r = 0, 0
        
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
                
            elif nums1[l] > nums2[r]:
                r += 1
                
            elif nums1[l] == nums2[r]:
                res.add(nums1[l])
                l += 1
                r += 1
                
        return list(res)