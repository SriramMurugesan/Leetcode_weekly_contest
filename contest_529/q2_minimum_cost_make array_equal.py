
class Solution:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')

        i = 0

        while i < n:
            j = i

            # Find the consecutive group
            while j + 1 < n and nums[j] == nums[j + 1]:
                j += 1

            # Check whether a valid operation index exists
            if i < n - 1 and j > 0:

                value = nums[i]

                # Prefix operation cost
                prefix_cost = i * value

                # Suffix operation cost
                suffix_cost = (n - j - 1) * value

                # Combined cost
                cost = prefix_cost + suffix_cost

                ans = min(ans, cost)

            i = j + 1

        return ans
