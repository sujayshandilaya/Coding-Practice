class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length= len(strs)
        flag=0
        prefix=''
        res = min(len(ele) for ele in strs)
        i=0
        while i<res:
            alpha=strs[0][i]
            for j in range(1,len(strs)):
                if(alpha==strs[j][i]):
                    pass
                else :
                    
                    return(prefix)
                    break
            i+=1
            prefix=prefix+alpha
            print(prefix)
        return(prefix)