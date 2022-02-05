class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        setchar,op=set(),set()
        i,j=0,10
        while j<=len(s):
            new_str=s[i:j]
            if new_str in setchar: op.add(new_str)
            else: setchar.add(new_str)
            i+=1
            j+=1
        
        return op

#####################

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cntr= Counter([s[i:i+10] for i in range(len(s)-9)] )
        return [k for k,v in cntr.items() if v>1]
