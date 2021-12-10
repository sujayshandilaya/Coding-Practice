class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        for operator in operations:
            if (operator=='++X' or operator=='X++'):
                x+=1
            else:
                x-=1
        return(x)
        
