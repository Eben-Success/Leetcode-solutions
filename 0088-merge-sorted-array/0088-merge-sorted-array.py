class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l, r = 0, 0
        
        while l < len(nums1) and r < len(nums2):
            if nums1[l] != 0:
                l += 1
                
            else:
                nums1[l] = nums2[r]
                r += 1
                
        return nums1.sort()
        