class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count,dict_num=0,{}
        for i in range(len(nums)):
            if nums[i] in dict_num:
                count+=dict_num[nums[i]]
                dict_num[nums[i]]+=1     
            else:
                dict_num[nums[i]]=1
          
        return(count)