class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict={}
        for i in range(len(nums)):
            if nums[i] in temp_dict.keys():
                return([temp_dict[nums[i]],i])
            else:
                temp_dict[target-nums[i]]=i
        
            
        