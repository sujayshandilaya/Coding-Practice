class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt={}
        
        for num in nums:
            cnt[num]=cnt.get(num,0)+1
        
        return sorted(sorted(nums, reverse=True), key=lambda i : cnt[i])