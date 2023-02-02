class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {char: i for i, char in enumerate(s)}
        j = anchor = 0
        result = []
        
        for i, char in enumerate(s):
            j = max(j, last[char])
            if i == j:
                result.append(i - anchor + 1)
                anchor = i + 1
        return result