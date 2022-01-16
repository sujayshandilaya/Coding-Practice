
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        distance=sys.maxsize
        for i in range(len(nums)):
            if nums[i]==target:
                distance=min(distance, abs(i-start))
                if distance==0: return 0
        
        return distance