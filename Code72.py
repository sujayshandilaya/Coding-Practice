class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    count+=1
        
        return count

#############
"""
Counter() returns the frequency dictionary fot the given items. For all the key, values in the dictionary, check if the target starts with the key. if it does, then calulate the suffix i.e. remaining part. CHeck for the no of times suffix is there and multiply it with the no of time that value is present. 
Exclude those counts where suffix is same as the given key.

return sum of all the counts.
 
"""
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        print(freq)
        
        ans=0
        
        for k,v in freq.items():
            if target.startswith(k):
                suffix=target[len(k):]
                ans+= v*freq[suffix]
                if k==suffix: ans-=freq[suffix]
        
        return(ans)
        