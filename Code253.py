class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_height,height=0,0
        for n in gain:
            max_height=max(max_height, n+height)
            height+=n
        
        return max_height