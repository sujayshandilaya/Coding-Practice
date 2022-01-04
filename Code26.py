

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
            
####################
# Same as 2nd
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        length=start=i=0
        new_dict={}
        n=len(s)
        if n==0 or n==1:
            return n

        while i < len(s):
            if s[i] in new_dict and start<=new_dict[s[i]]:
                start=new_dict[s[i]]+1
                length=i-start+1
                print(start,s[i])
            else:
                length+=1
                max_len=max(length,max_len)

            new_dict[s[i]]=i
            i+=1  
        
        return(max_len)

# start<= new_dict[s[i]], ensures that the values before the start are not considered for comparison.  
#which condition to mention in if and else is important, especially if  
 
tmmzuxt
0123456
        
 max_len=Start=0
 
 t:0, m:1
 
 start=2
 max_len=2
 t:0, m:2,z:3,u:4
 