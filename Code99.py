class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt=Counter(s)
        
        val=cnt[s[0]]
        
        for value in cnt.values():
            if value!=val:
                return False
        
        return True

###########

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1