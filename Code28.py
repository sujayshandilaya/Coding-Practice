class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dict_num={'2':['a','b','c'],
                  '3':['d','e','f'],
                  '4':['g','h','i'],
                  '5':['j','k','l'],
                  '6':['m','n','o'],
                  '7':['p','q','r','s'],
                  '8':['t','u','v'],
                  '9':['w','x','y','z']
                 }
        
        if digits=="":
            return([])
        op=dict_num[digits[0]]
        for k in range (1,len(digits)):
            temp=[]
            for i in op:
                for j in dict_num[digits[k]]: 
                    temp.append(i+j)
            op=temp
        return(op)
        

###########

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dict_num={'2':['a','b','c'],
                  '3':['d','e','f'],
                  '4':['g','h','i'],
                  '5':['j','k','l'],
                  '6':['m','n','o'],
                  '7':['p','q','r','s'],
                  '8':['t','u','v'],
                  '9':['w','x','y','z']
                 }
           
        
        op = [''] if digits else []
        
        for k in range (0,len(digits)):
            temp=[]
            temp = [ i+j for i in op for j in dict_num[digits[k]] ]
            op=temp
        return(op)
        

            