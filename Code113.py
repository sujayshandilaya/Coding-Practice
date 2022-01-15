class Solution:
    def groupThePeople(self, sizes: List[int]) -> List[List[int]]:
        group={}
        res=[]
        
        for i in range(len(sizes)):
            if sizes[i] in group:
                group[sizes[i]].append(i)
            else:
                group[sizes[i]]=[i]

            if len(group[sizes[i]])==sizes[i]:
                res.append(group[sizes[i]])
                group[sizes[i]]=[]
        
        return(res)

###############

class Solution:
    def groupThePeople(self, sizes: List[int]) -> List[List[int]]:
        group=defaultdict(list)
        res=[]

        for k,v in enumerate(sizes):
            group[v].append(k)
            if len(group[v])==v:
                res.append(group[v])
                group[v]=[]
        
        return(res)
            