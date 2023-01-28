class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort them by their left point.
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        right_end = float("-inf")
        for interval in intervals:
            if interval[1] > right_end:
                count += 1
                right_end = interval[1]
        return count
        