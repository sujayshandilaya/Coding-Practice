class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1=version1.split('.')
        ver2=version2.split('.')
        
        for compare in zip_longest(ver1,ver2, fillvalue=0):
            if int(compare[0]) < int(compare[1]):
                return -1
            if int(compare[0]) > int(compare[1]):
                return 1
        
        return 0

##################

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1=version1.split('.')
        ver2=version2.split('.')
        
        l1,l2= len(ver1), len(ver2)
        
        if l1<l2:
            ver1 += (['0']*(l2-l1))
        else:
            ver2 += (['0']*(l1-l2))

        for compare in zip(ver1,ver2):
            if int(compare[0]) < int(compare[1]):
                return -1
            if int(compare[0]) > int(compare[1]):
                return 1
        
        return 0