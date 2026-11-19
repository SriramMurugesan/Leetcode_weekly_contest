class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        count = 0
        for i in range(len(nums)):
            min_val=nums[i]
            and_val=nums[i]
            for j in range(i,len(nums)):
                min_val = min(min_val,nums[j])
                and_val = and_val & nums[j]
                if min_val == and_val:
                    count+=1
        return count