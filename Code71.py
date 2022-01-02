class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        destDict={}
        
        for path in paths:
            destDict[path[0]]=path[1]
        
        for v in destDict.values():
            if v not in destDict.keys():
                return v
#######Set is faster implementation thn dictionary. dictionary also consumes higehr memory than set.

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        s = set(p[0] for p in paths)                  
        for path in paths:
            if path[1] not in s:                         
                return path[1]