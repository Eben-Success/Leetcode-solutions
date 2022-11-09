class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        
        temp = ""
        
        int_nums = [int(item) for item in nums]
        
        srt = sorted(int_nums, reverse=True)
        
        return str(srt[k-1])
        