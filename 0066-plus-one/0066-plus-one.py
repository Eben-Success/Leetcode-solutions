class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = [str(i) for i in digits]
        int_val = int("".join(ans)) + 1
        return list(str(int_val))
                    