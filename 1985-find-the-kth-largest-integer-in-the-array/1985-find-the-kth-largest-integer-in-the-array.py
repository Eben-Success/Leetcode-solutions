class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        
        temp = ""
        
        # Convert string into integers
        int_nums = [int(item) for item in nums]
        
        # Sort integers in descending order
        srt = sorted(int_nums, reverse=True)
        
        # return the element at the index of k - 1
        return str(srt[k-1])
        