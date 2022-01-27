class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        new_dict=defaultdict(int)
        
        new_dict[0]=1
        cnt=sum_till_now=0
        
        for num in nums:
            sum_till_now+=num
            sum_till_now%=k
            
            cnt+=new_dict.get(sum_till_now,0)
            new_dict[sum_till_now]=new_dict.get(sum_till_now,0)+1
        
        return cnt