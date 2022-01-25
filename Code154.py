class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_dict={0:1}
        
        cnt=sum_till_now=0
        for num in nums:
            sum_till_now+=num
            cnt+=freq_dict.get((sum_till_now-k),0)
            freq_dict[sum_till_now]= freq_dict.get(sum_till_now,0)+1
        
        return(cnt)

#PrefixSum
#https://www.youtube.com/watch?v=20v8zSo2v18