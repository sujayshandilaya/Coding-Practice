class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_cnt=max(candies)
        
        op=[True if candy+extraCandies >= max_cnt else False for candy in candies]
        print(max_cnt)
        return op
		
################

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_cnt=max(candies)
        diff=max_cnt-extraCandies        
        op=[True if candy>= diff else False for candy in candies]
        print(max_cnt)
        return op