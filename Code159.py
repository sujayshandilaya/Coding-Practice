class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic_s,dic_p={},{}
        output=[]
        for letter in p:
            dic_p[letter]=dic_p.get(letter,0)+1
        i=0
        for j in range(len(s)):
            dic_s[s[j]]=dic_s.get(s[j],0)+1
            if j >= len(p)-1:
                if dic_s==dic_p:
                    output.append(i)
                dic_s[s[i]]-=1
                if dic_s[s[i]]==0:
                    del dic_s[s[i]]
                i+=1
        return output

#####################
#Comparing dictionaries is much slower than comparing lists. Hence we should prefer lists if possible.
 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic_s,dic_p=[0]*26,[0]*26
        output=[]
        for letter in p:
            index=ord(letter)-97
            dic_p[index]+=1
        i=0
        for j in range(len(s)):
            index=ord(s[j])-97
            dic_s[index]+=1
            if j >= len(p)-1:
                if dic_s==dic_p:
                    output.append(i)
                dic_s[ord(s[i])-97]-=1
                i+=1
        return output
