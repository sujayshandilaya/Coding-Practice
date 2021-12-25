class Solution:
    def nextPermutation(self,nums):

        def search(arr,N):
            min_num=arr[0]
            min_index=0
            for i in range(1,len(arr)):
                if arr[i]<=N :
                    pass
                else:
                    if arr[i]<=min_num:
                        min_num=arr[i]
                        min_index=i
            return(min_index)

        i=0
        flag=1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                flag=0
                print(i)
                print("isnde if")
                num=search(nums[i+1:], nums[i])
                print(num)
                nums[i], nums[i+1+num] = nums[i+1+num],nums[i]
                print(nums)
                nums[i+1:] = nums[i+1:][::-1]
                print(nums)
                break
            

        if(flag==1):
            nums.reverse()
        
        return nums

        