class Solution:
    def compress(self, chars: List[str]) -> int:
        
        s = ""
        count = 0
        prev_char = chars[0]
        for char in chars:
            if char == prev_char:
                count += 1
            else:
                s += prev_char
                if count > 1:
                    s += str(count)
                prev_char = char
                count = 1
        s += prev_char
        if count > 1:
            s += str(count)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)