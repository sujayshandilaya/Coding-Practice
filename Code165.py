class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        output=[]
        for i in range(len(l)):
            arr=nums[l[i]:r[i]+1]
            arr.sort()
            diff=arr[1]-arr[0]
            j=1
            while j<len(arr)-1:
                if arr[j+1]-arr[j] != diff:
                    output.append(False)
                    break
                j+=1
            else:
                output.append(True)
        return output

#########################

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkArithmetic(arr: List[int]):
            if len(arr)==2:
                return True
            min_num=min(arr)
            max_num=max(arr)
            if min_num==max_num:
                return True
            
            diff=int((max_num-min_num)//(len(arr)-1))
            
            if (max_num-min_num)%(len(arr)-1)!=0:
                return False

            res=[1]*(len(arr))
            for num in arr:
                if (num-min_num)%diff !=0:
                    return False
                res[(num-min_num)//diff]=0  
            if 1 in res:
                return False
            return True
        
        output=[]
        for i in range(len(l)):
            arr=nums[l[i]:r[i]+1]
            output.append(checkArithmetic(arr))      
        return output
            
        
            
        