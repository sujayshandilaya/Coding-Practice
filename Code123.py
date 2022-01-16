class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        li,P=[],[]
        for i in range(1,m+1):
            P.append(i)
        
        for i in range(0, len(queries)):
            index=P.index(queries[i])
            P.remove(queries[i])
            P.insert(0,queries[i])
            li.append(index)

        return li
        