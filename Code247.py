class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
        input_dict={'type':0,'color':1,'name':2}
        cnt=0
        for item in items:
            if item[input_dict[ruleKey]]==ruleValue:
                cnt+=1
        
        return cnt
		
###############################

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):

        input_dict={'type':0,'color':1,'name':2}
        cnt=sum(1 if item[input_dict[ruleKey]]==ruleValue else 0 for item in items)
        
        return cnt