class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt=0
        for word in words:
            cntr=Counter(chars)
            for i in range(len(word)):
                if word[i] in cntr and cntr[word[i]] >0:
                    cntr[word[i]]-=1
                else : break
            else:
                cnt+=len(word)
        return cnt