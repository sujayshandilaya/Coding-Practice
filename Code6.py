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

#########

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len=min([len(ele) for ele in strs])
        cnt=""
        for i in range(min_len):
            letter=strs[0][i]
            for ele in strs:
                if ele[i]!=letter:
                    return cnt
            cnt+=letter
        
        return cnt

######################
class Solution:
    def longestCommonPrefix(self, S: List[str]) -> str:
        if not S: return ''
        m, M, i = min(S), max(S), 0
        print(m,M)
        for i in range(min(len(m),len(M))):
            if m[i] != M[i]: break
        else: 
            print(i)
            i += 1
        return m[:i]
 #refer this link for for else block. Else is only executed in the case when break is not executed. if loop doesnt run at all , then also the else blovk is executed.       
#https://mail.python.org/pipermail/python-ideas/2009-October/006155.html
