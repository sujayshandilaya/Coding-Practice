class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals=sorted(intervals, key = lambda x: x[0])
        
        li=intervals[0]
        op=[]
        for interval in intervals:
            if li[0]<=interval[0]<=li[1]:
                li[1] = max(interval[1],li[1])
            else:
                op.append(li)
                li=list(interval)
        op.append(li)
        return op