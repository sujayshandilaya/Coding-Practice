class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        num1,num2=0,0
        op=set()
        if x==1:
            num1=1
        else:
            while (pow(x,num1)) < bound:
                num1+=1
        if y==1:
            num2=1
        else:
            while (pow(y,num2)) < bound:
                num2+=1
        
        for i in range(num1):
            for j in range(num2):
                n=pow(x,i)+pow(y,j)
                if n<=bound:
                    op.add(n)
        return op

#########################

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x==1 and y==1:
            if bound>=2:return [2]    
            else: return []
        op=set()
        if x>y:
            x,y=y,x
        
        if x==1:
            j=0
            while (pow(y,j)) < bound:
                op.add(pow(y,j)+1)
                j+=1    
                    
            return op
                
        num1,num2=bound//x,bound//y
        
        for i in range(num1+1):
            if pow(x,i)>bound: break   
            for j in range(num2+1):
                if pow(y,j)>bound: break
                n=pow(x,i)+pow(y,j)
                if n<=bound:
                    op.add(n)
        return op