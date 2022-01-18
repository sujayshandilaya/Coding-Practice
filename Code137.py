class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        length=max([len(ele) for ele in s])
        new_s=[ele.ljust(length) for ele in s]
        li=[]
        for word in zip(*new_s):
            li.append((''.join(word)).rstrip())
		
		#li = ["".join(word).rstrip() for word in zip(*new_s)]
		# insdtead of for loop, we can do this in one line
        
        return(li)