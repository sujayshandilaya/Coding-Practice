for i in words1:
            if words1.count(i)==1 and words2.count(i)==1:
                count += 1
                
        return count

#########
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1,c2=Counter(words1),Counter(words2)
        cnt=0
        for k,v in c1.items():
            if v==1 and c2.get(k,0)==1:
                cnt+=1
        
        return cnt