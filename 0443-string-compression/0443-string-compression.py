class Solution:
    def compress(self, chars: List[str]) -> int:
        
        """
        We can solve this problem in two ways.
        The first approach uses an extra space and also has a time complexity of O(n).
        However, the second approaches uses constant time."""
        
        # The first approach
        # Time: O(n) 
        # Space O(n)
        
        """
        1. Initialize an empty string `s` and a variable count to 0.
        2. Iterate through the characters in `chars`.
            - If the current character is the same as the previous character, increment `count`.
            - Otherwise, append the previous character to `s` and reset `count` to 1 since we are
            on a different character.
        3. At the end, append the last character and its count to `s`.
        4. Replace the characters in  `chars` with the characters in `s`."""
        
#         s = ""
#         count = 0
#         prev_char = char[0]
        
#         for char in chars:
#             if char == prev_char:
#                 count += 1
#             else:
#                 s += prev_char
#                 if count > 1:
#                     s += str(count)
#                 prev_char = char
#                 count = 1
#         s += prev_char
#         if count > 1:
#             s += str(count)
#         for i in range(len(s)):
#             char[i] = s[i]
#         return len(s)

        count = 0
        prev_char = chars[0]
        i = 0
        for char in chars:
            if char == prev_char:
                count += 1
            else:
                chars[i] = prev_char
                i += 1
                if count > 1:
                    for c in str(count):
                        chars[i] = c
                        i += 1
                prev_char = char
                count = 1
        chars[i] = prev_char
        i += 1
        if count > 1:
            for c in str(count):
                chars[i] = c
                i += 1
        return i




        
        
        
        
        
        
        