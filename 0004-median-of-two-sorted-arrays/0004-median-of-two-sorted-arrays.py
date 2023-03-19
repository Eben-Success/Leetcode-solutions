class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1 += nums2
        
        nums1.sort()
        
        if len(nums1) % 2 != 0:
            mid = len(nums1) // 2
            return nums1[mid]
        
        else:
            l, r = 0, len(nums1) - 1
            
            while l < r:
                mid = (l + r) // 2
                
                res = nums1[mid] + nums1[mid+1]
                
                return res/2
        