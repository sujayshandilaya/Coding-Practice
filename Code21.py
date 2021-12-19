class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict={}
        for i in nums:
            if i in count_dict.keys():
                count_dict[i]= count_dict.get(i)+1
            else:
                count_dict[i]=1
        
        n= max(i for i in count_dict.values())
        for key, value in count_dict.items():
            if value == n:
                return key