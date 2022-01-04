class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        result=[None]*len(nums)
        for i in range(len(nums)):
            cnt=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    cnt+=1
            result[i]=cnt
        
        return(result)


#######
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict_num,result={},[]
        new_nums=sorted(nums)
        n=len(nums)
        for i in range(n):
            if new_nums[i] not in dict_num:
                dict_num[new_nums[i]]=i
        
        for num in nums:
            result.append(dict_num[num])
        
        return(result)
		
'''
The catch in this solution is that, after sorting the element, the no of elements less than the current elemnt is equal to the index. 

Also, if the element is present multiple times, then only the first occurence of that element is taken into consideration.
'''