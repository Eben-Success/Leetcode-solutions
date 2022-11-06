class Solution:
    def sortSentence(self, s: str) -> str:
        
        # split sentence into words
        splt = s.split(" ")
        
        # sort words by numbers
        srt = sorted(splt, key=lambda w: w[-1])
        
        # extract words and remove numbers
      
        word = [w[:-1] for w in srt]
        return " ".join(word)
            
        