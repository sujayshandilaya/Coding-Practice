class Solution:
    def isValid(self, s: str) -> bool:
        valid={')':'(','}':'{',']':'['}
        temp=['N']
        for bracket in s:
            if bracket in valid.keys():
                if temp.pop() != valid[bracket]:
                    return False
            else:
                temp.append(bracket)
        
        return True if len(temp) == 1 else False