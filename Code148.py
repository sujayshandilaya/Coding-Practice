class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans,l,r=0,0,0
        for r in range(len(nums)):
            if nums[r]==0:
                if k==0:
                    while(nums[l]!=0): l+=1
                    l+=1
                else:
                    k-=1
            ans=max(ans, r-l+1)
        return(ans)

#The important logic here is that we need to find longest substring which contains k no of zeroes.
#longest substring with k zeroes, will automatically be longest with 1s converted to 0.

#As per the logic, we keep count of k, whenever k ==0, we move the left counter till next 0 and compare the length with our original lenght