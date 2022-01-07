class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_list=s.split(" ")
        if len(pattern) != len(s_list):
            return False
        else:
            pattern_dict={}
            for i in range(len(pattern)):
                if pattern[i] in pattern_dict.keys() and pattern_dict[pattern[i]] != s_list[i]:
                    return False                    
                elif pattern[i] not in pattern_dict.keys() and s_list[i] in pattern_dict.values():
                    return False
                else:
                    pattern_dict[pattern[i]]=s_list[i]
            return True