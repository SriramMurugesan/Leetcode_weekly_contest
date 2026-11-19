
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        left = [-1] * n
        stack = []
        # Find left boundaries
        for i, x in enumerate(nums):
            while stack and (nums[stack[-1]] & x) == x:
                stack.pop()
            if stack:
                left[i] = stack[-1]

            stack.append(i)
        stack = []
        ans = 0
        # Find right boundaries and count
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while stack and nums[stack[-1]] != x and (nums[stack[-1]] & x) == x:
                stack.pop()
            right = stack[-1] if stack else n
            stack.append(i)
            ans += (i - left[i]) * (right - i)
        return ans
