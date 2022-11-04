class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        temp_dict={'b':0,'a':0,'l':0,'o':0,'n':0}
        for s in text:
            if s in ['b','a','l','o','n']:
                temp_dict[s]+=1
        
        return int(min(temp_dict['b'], temp_dict['a'], temp_dict['l']/2, temp_dict['o']/2,temp_dict['n']))
        