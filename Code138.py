class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        
        new=[word[::-1] for word in s]
        
        return(' '.join(new))

#####

class Solution:
    def reverseWords(self, s: str) -> str:
        
        i,j=0,0
        n=len(s)
        words=[]
        while i<=n:
            word=[]
            while j<n and s[j]!=' ':
                word.insert(0,s[j])
                j+=1
            words.append(''.join(word))
            i=j+1
            j=i
        return(' '.join(words))

#######################

class Solution:
    def reverseWords(self, s: str) -> str:
        i,j=0,0
        n=len(s)
        words=''
        while i<=n:
            word=[]
            while j<n and s[j]!=' ':
                j+=1
            words+=(s[i:j][::-1]+' ')
            i=j+1
            j=i

        return(words.strip())

        
      