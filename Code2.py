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

########################
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return( sum(1 if '+' in i else -1 for i in operations))
        
###############

def finalValueAfterOperations(self, operations: List[str]) -> int:
        op_dict = {"--X" : -1, "X--" : -1,
                 "++X" : 1, "X++" : 1}
        return sum(op_dict[op] for op in operations)
