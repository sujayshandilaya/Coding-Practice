class Solution:
    def frequencySort(self, s: str) -> str:
        output=[]
        freq=Counter(s)
        
        sort_freq={k:v for k,v in sorted(freq.items(), key = lambda x: x[1], reverse = True)}
        
        for k,v in sort_freq.items():
            output+=[k]*v
        
        return "".join(output)
        