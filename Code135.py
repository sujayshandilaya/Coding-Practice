class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt=0
        for char in zip(*strs):
            if list(char) != sorted(char):
                cnt+=1
        
        return(cnt)

###############

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt=0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                print(strs[j][i] , strs[j+1][i])
                if strs[j][i] > strs[j+1][i]: 
                    
                    cnt+=1
                    break # else cnt=cnt
        
        return cnt
        
#########
#same sol as previous one
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = 0

        for col in range(len(strs[0])): #  start at the column - [0,0]
            for row in range(len(strs)-1): # move down the column - [0,0]
                if strs[row][col] > strs[row+1][col]: # check if the current row is greater than the row below it - strs[0][0] > strs[1][0]?
                    res += 1 # if it is, it means that this column is not sorted and we add a count 
                    break # don't continue looking at this column since it's not sorted, move onto the next column
        return res