class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        rule_dict={'type':0, 'color':1, 'name':2}
        
        cnt=0
        
        for item in items:
            if item[rule_dict[ruleKey]]==ruleValue:
                cnt+=1
        
        return(cnt)
        