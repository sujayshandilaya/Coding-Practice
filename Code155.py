class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        sum_till_now=0
        freq_dict={0:-1}
        
        for i in range(len(nums)):
            sum_till_now+=nums[i]
            sum_till_now=sum_till_now%k
            
            if sum_till_now in freq_dict and (i-freq_dict[sum_till_now])>1:
                return True
            
            if sum_till_now not in freq_dict:
                freq_dict[sum_till_now] = i
        
        return False
            
            