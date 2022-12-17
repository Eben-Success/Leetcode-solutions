class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        # Time: O(mlogm + nlogn)
        # Space: O(sorting) | O(1)
        
        nums1.sort(), nums2.sort()
        nums1.sort(), nums2.sort()
        
        l = r = 0
        res = []
        
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                res.append(nums1[l])
                l += 1
                r += 1
        return res
        
        