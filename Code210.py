class Solution:
    def maxArea(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        
        h= [0]+sorted(h)+[m]
        v= [0]+sorted(v)+[n]
        
        max_h=max([h[i+1]-h[i] for i in range(len(h)-1)])
        max_v=max([v[i+1]-v[i] for i in range(len(v)-1)])
        
        return((max_h*max_v)%(pow(10,9)+7))