class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s_new=list(s) 
        print(s_new)
        temp=[]
        temp_list=[]
        op=""
        for p in s_new:
            temp_list.append(p)
            if p=='(':
                temp.append(p)
            else:
                print(p)
                temp.pop()
                if len(temp)==0:
                    op+="".join(temp_list[1:-1])
                    temp_list=[]
        return op