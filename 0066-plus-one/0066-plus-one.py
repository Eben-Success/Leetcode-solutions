class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        l = len(digits)
        i = 1
        
        while i<=l:
            if digits[-i]!=9:
                digits[-i]+=1;
                return digits
            else:
                digits[-i]=0
                i+=1
        return [1]+digits
        
        