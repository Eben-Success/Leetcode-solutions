class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        res = -1
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                res = i
        if res == -1:
            return ""
        else:
            return str(num[0:res+1])