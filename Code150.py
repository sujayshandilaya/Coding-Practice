class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        j,cnt=0,0
        vowels=('a','e','i','o','u') #vowels can be defined as set or list or string. String is fastest of all and takes least space
        #vowels="aeiou"
        for j in range(k):
            if s[j] in vowels:
                cnt+=1
        max_cnt=cnt
        for j in range(k,len(s)):
            if s[j-k] in vowels:
                cnt-=1
            if s[j] in vowels:
                cnt+=1
            max_cnt=max(max_cnt,cnt)
        return(max_cnt)
