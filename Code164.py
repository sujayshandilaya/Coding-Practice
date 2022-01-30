class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        temp=defaultdict(set)
        res=[0]*k
        for log in logs:
            temp[log[0]].add(log[1])
        
        for v in temp.values():
            res[len(v)-1]+=1
        
        return res