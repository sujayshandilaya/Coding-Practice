

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        if(s==''):
            return(0)
        else:
            max_len=1
            for i in range(len(s)):
                letters=set()
                for j in range(i,len(s)):
                    if s[j] in letters:
                        print("inside if")
                        max_len= max(max_len,(j-i))
                        break  
                    else:
                        letters.add(s[j])
                        max_len= max(max_len,len(letters))
            return(max_len)
               
			   
			   
			   
#Solution 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        letters={}
        start=max_len=0
        
        for i in range(len(s)):
            if s[i] in letters and start <= letters[s[i]]:
                start = letters[s[i]]+1 
            else:
                max_len= max(max_len, i-start+1)
            letters[s[i]]=i
        return(max_len)
            
            
tmmzuxt
0123456
        
 max_len=Start=0
 
 t:0, m:1
 
 start=2
 max_len=2
 t:0, m:2,z:3,u:4
 