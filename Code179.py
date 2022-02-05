class Solution:
    def prisonAfterNDays(self, nums: List[int], n: int) -> List[int]:
        li=[]
        s=[]
        for i in range(1,n+1):
            temp=list(nums)
            temp[0],temp[7] = 0,0
            for j in range(1,7):
                if nums[j-1]==nums[j+1]:
                    temp[j]=1
                else: temp[j]=0
            nums=list(temp)
            if nums in s:
                return s[n%(i-1)-1]
            else:
                s.append(nums)
        return nums

##################################

class Solution:
    def prisonAfterNDays(self, nums: List[int], n: int) -> List[int]:
        n=(n-1)%14+1
        for i in range(1,n+1):
            temp=list(nums)
            temp[0],temp[7] = 0,0
            for j in range(1,7):
                if nums[j-1]==nums[j+1]:
                    temp[j]=1
                else: temp[j]=0
            nums=list(temp)
        return nums 