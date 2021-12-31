class Solution:
    def interpret(self, command: str) -> str:
        
        string=''
        i=0
        while i < len(command):
            if command[i]=="G":
                string+='G'
                i+=1
            elif command[i]=="(" and command[i+1]==")" :
                string+='o'
                i+=2
            elif command[i]=="(" and command[i+1]=='a':
                string+='al'
                i+=4
        return(string)
##########################
class Solution:
    
    def interpret(self, s: str) -> str:
        d = {"(al)":"al", "()":"o","G":"G"}
        tmp= ""
        res=""
        for i in range(len(s)):
            tmp+=s[i]
            if(tmp in d):
                res+=d[tmp]
                tmp=""
        return res

########################
class Solution:
    
    def interpret(self, s: str) -> str:
        return (s.replace('()','o').replace('(al)','al'))