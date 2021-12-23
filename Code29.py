class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_word={}
        
        for word in strs:
            key = ''.join(sorted(word))
            if key in dict_word:
                dict_word[key].append(word)
            
            else:
                dict_word[key]=[word]
                
        return([v for v in dict_word.values()])
      

##########

class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()