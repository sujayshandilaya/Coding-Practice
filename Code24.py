#When you use set function to convert a list to a set, it is a time-consuming operation. This solution is concise but inefficient.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num=set()
        
        for i in nums:
            if i in num:
                return True
            else:
                num.add(i)
        return False

#Alternate Solution:

# COnevrt List to set and compare the lengths of both. If length is not equal return false.

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))