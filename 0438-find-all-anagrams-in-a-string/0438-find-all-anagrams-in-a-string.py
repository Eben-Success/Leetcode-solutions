class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_freq = defaultdict(int)
        for c in p:
            p_freq[c] += 1
            
        s_freq = defaultdict(int)
        for c in s[:len(p)]:
            if c in p_freq:
                s_freq[c] += 1
            
        res = []
        if p_freq == s_freq:
            res.append(0)
            
        for i in range(len(p), len(s)):
            if s[i-len(p)] in s_freq:
                s_freq[s[i-len(p)]] -= 1
                if s_freq[s[i-len(p)]] == 0:
                    del s_freq[s[i-len(p)]]
            if s[i] in p_freq:
                s_freq[s[i]] += 1
                
            # check for anagram
            if p_freq == s_freq:
                res.append(i - len(p) + 1)
                
        return res