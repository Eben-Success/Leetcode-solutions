class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        score = 0
        l, r = 0, len(tokens) - 1
        
        while l <= r and (score or power >= tokens[l]):
            
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
                
            elif l != r:
                score -= 1
                power += tokens[r]
                r -= 1
            
            else:
                break
                
        return score