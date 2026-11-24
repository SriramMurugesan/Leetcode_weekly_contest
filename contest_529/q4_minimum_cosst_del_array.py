class Solution:
    def minCost(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0
        even = 0
        odd = float("inf")
        for x in nums[1:-1]:
            new_even = min(even,odd+x)
            new_odd = min(odd,even+x)
            even = new_even
            odd = new_odd
        return nums[0]+nums[-1]+even 