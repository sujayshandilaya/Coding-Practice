class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        set_num=set()
        op=[]
        
        for n in nums:
            if n in set_num:
                op.append(n)
            else:
                set_num.add(n)
        return op

####################

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        op=[]
        for n in nums:
            n=abs(n)
            if nums[n-1]<0:
                op.append(n)
            else:
                nums[n-1] = (-1*nums[n-1])
        return op