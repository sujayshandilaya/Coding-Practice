class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        
        new_arr=arr1+arr2+arr3
        cntr=Counter(new_arr)
        op=[]
        for k,v in cntr.items():
            if v==3:
                op.append(k)
        
        return op


