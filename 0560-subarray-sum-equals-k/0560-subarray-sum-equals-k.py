class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        new_dict={0:1}
        sum_till_now=cnt=0
        
        for num in nums:
            sum_till_now+=num
            
            cnt+=new_dict.get(sum_till_now-k,0)
            new_dict[sum_till_now]=new_dict.get(sum_till_now,0)+1
            #print(new_dict)
        return cnt
