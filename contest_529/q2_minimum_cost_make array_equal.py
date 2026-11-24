class Solution:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')

        i = 0

        while i < n:
            j = i

            # Find the end of the consecutive group
            while j + 1 < n and nums[j] == nums[j + 1]:
                j += 1

            length = j - i + 1

            # Check whether the group has a valid internal index
            if i < n - 1 and j > 0:
                cost = nums[i] * (n - length)
                ans = min(ans, cost)

            # Move to the next group
            i = j + 1

        return ans