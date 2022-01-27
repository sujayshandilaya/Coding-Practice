class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        sum_till_now,cnt=0,0
        freq_dict={0:1}
        
        for num in nums:
            sum_till_now+=num
            if sum_till_now-goal in freq_dict:
                cnt+=freq_dict[sum_till_now-goal]
            freq_dict[sum_till_now]= freq_dict.get(sum_till_now,0)+1
        
        return cnt
        