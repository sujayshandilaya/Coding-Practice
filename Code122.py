class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
            
            add=0
            for n in range(1, len(arr)+1,2):
                for i in range(len(arr)):
                    if i+n > len(arr):
                        break
                    else:
                        add+=sum(arr[i:i+n])
            
            return add