class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_set=set()
        for n in arr:
            if (n*2) in arr_set or (n/2) in arr_set:
                return True
            else:
                arr_set.add(n)
        return False