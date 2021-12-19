class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_letter={}
        if (len(s)==1 or s is None):
            return True
        else:
            for i in range(0, len(s)):
                if s[i] in dict_letter.keys() and dict_letter[s[i]]==t[i]:
                    pass
                elif s[i] not in dict_letter.keys() and t[i] not in dict_letter.values():
                    dict_letter[s[i]] = t[i]
                else:
                    return False
            return True
                    
                
        
        