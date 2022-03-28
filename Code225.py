class Solution:
    def countKDifference(self, nums: List[int], target: int) -> int:
        num_dict={}
        cnt=0
        for i in range(len(nums)):
            num_dict[nums[i]+target]=num_dict.get(nums[i]+target,0)+1
            num_dict[nums[i]-target]=num_dict.get(nums[i]-target,0)+1
        for i in range(len(nums)):
            if nums[i] in num_dict:
                cnt+=num_dict.get(nums[i])
        return int(cnt/2)
###################
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = {}
        count = 0        
        for n in nums:
            count += seen.get(n + k, 0) + seen.get(n - k, 0)
            seen[n] = seen.get(n, 0)+1
        return count
########################

class Solution:
    def countKDifference(self, nums: List[int], target: int) -> int:
        cnt=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j])==target:
                    cnt+=1 
        return cnt