class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict={}
        
        for i in range(len(nums)):
            if nums[i] in num_dict:
                num_dict[nums[i]]+=1
            else:
                num_dict[nums[i]]=1
        
        for k,v in num_dict.items():
            if v==1:
                return k

##############

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict=Counter(nums)  
     
        for k,v in num_dict.items():
            if v==1:
                return k

################

#2*(a+b+c) - (a+a+b+b+c) -> this will return c. element which occurs only once

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = (2*(sum(set(nums))) - sum(nums))
        return(num)