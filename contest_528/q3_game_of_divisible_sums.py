class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [None] * n
        def dfs(u):
            if u == n:
                return 0 
            if dp[u] is not None:
                return dp[u]
            max_val = float("-inf")
            # Choice 1: Take one element
            s = nums[u] 
            if s % 3 == 0:
                result = s - dfs(u + 1) 
            else:
                result = s + dfs(u + 1)
            max_val = max(max_val, result)
            # Choice 2: Take two elements
            if u + 1 < n:
                s = nums[u] + nums[u + 1]
                if s % 3 == 0:
                    result = s - dfs(u + 2)
                else:
                    result = s + dfs(u + 2)
                max_val = max(max_val, result)
            dp[u] = max_val
            return dp[u]
        return dfs(0)