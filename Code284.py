##########
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return "111" in "".join([str(i%2) for i in arr])
		
################
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        for i in range(1, len(arr)-1):
            if (arr[i-1]%2!=0 and arr[i]%2!=0 and arr[i+1]%2!=0):
                return True
############

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cntr=0
        for i in range(len(arr)):
            if arr[i]%2!=0:
                cntr+=1
            else:
                cntr=0
            
            if cntr==3:
                return True
        return False