class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        #length=sum([len(ele) for ele in words])
        length=0
        word_list={}
        for i in words:
            for j in i:
                length+=1
                word_list[j]=word_list.get(j,0)+1
        
        
        if (length%len(words))==0:
            for v in word_list.values():
                if v%len(words)!=0:
                    return False
            return True
        else:
            return False

#############

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        matrix=[j for i in words for j in i]
        length=len(matrix)
        
        if (length%len(words))==0:
            for v in Counter(matrix).values():
                if v%len(words)!=0:
                    return False
            return True
        else:
            return False

###############

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        word_dict={}
        n=len(words)
        for i in words: 
                for j in i:
                    word_dict[j] = word_dict.get(j,0)+1

        for v in word_dict.values():
            if v%n!=0:
                return False
        
        return True
###############

class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        n=len(words)
        joint=''.join(words)
        
        for i in set(joint):
            if joint.count(i)%n!=0: return False
        
        return True
		



        
            
        