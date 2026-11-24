class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        count = 0
        n=len(nums)
        if len(nums)==1:
            return 1
        if nums[0]>= nums[1]:
            count+=1
        if  nums[n-1]>=nums[n-2]:
            count+=1
        for i in range(1,n-1):
            if ((nums[i-1]+nums[i+1])/2)<=nums[i]:
                count+=1
        return count
  

