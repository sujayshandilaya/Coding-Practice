class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        seen=set()
        bulls=cows=0
        c=Counter(secret)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                c[secret[i]]-=1
                seen.add(i)
            if secret[i]!=guess[i]:
                if guess[i] in c.keys() and c[guess[i]]>0: #and i not in seen:
                    cows+=1
                    c[guess[i]]-=1
        return("{}A{}B".format(bulls,cows)) # This method is much much faster than concat strings.
        #return(str(bulls)+'A'+str(cows)+'B')