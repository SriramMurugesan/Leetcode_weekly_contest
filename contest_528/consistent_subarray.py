"""
LeetCode Weekly Contest 528
Problem: Count Consistent Subarrays (I & II)
LeetCode Links:
- Part I: https://leetcode.com/problems/count-consistent-subarrays-i/
- Part II: https://leetcode.com/problems/count-consistent-subarrays-ii/

Difficulty:
- Part I: Easy (N <= 100)
- Part II: Hard (N <= 200,000)

Problem Statement:
Given an integer array `nums`, a subarray is defined as "consistent" if the
bitwise AND of all its elements is equal to the minimum value of that subarray.
Return the total number of consistent subarrays in `nums`.
"""

from typing import List


class Solution:
    def countConsistent(self, nums: List[int]) -> int:
        """
        Optimal O(N) Solution using Monotonic Stack & Bitwise Boundary Tracking.
        Works for both Part I (N <= 100) and Part II (N <= 200,000).

        Key Insight:
        For any non-negative subarray, bitwise AND <= min(subarray).
        Equality holds iff every element in the subarray contains every set bit of the minimum element.
        """
        n = len(nums)
        if n == 0:
            return 0

        # Monotonic stack: find previous strictly smaller element (<)
        stack = []
        prev_smaller = [-1] * n
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        # Monotonic stack: find next smaller or equal element (<=)
        stack = []
        next_smaller_or_equal = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                next_smaller_or_equal[i] = stack[-1]
            stack.append(i)

        # Track the latest position to the left where each bit (0..20) is 0
        last_zero = [-1] * 21
        left_bit_limit = [-1] * n
        for i in range(n):
            val = nums[i]
            limit = -1
            for b in range(21):
                if (val >> b) & 1:
                    if last_zero[b] > limit:
                        limit = last_zero[b]
                else:
                    last_zero[b] = i
            left_bit_limit[i] = limit

        # Track the earliest position to the right where each bit (0..20) is 0
        next_zero = [n] * 21
        right_bit_limit = [n] * n
        for i in range(n - 1, -1, -1):
            val = nums[i]
            limit = n
            for b in range(21):
                if (val >> b) & 1:
                    if next_zero[b] < limit:
                        limit = next_zero[b]
                else:
                    next_zero[b] = i
            right_bit_limit[i] = limit

        # Count subarrays where nums[i] is the unique minimum and bitwise AND == nums[i]
        total_count = 0
        for i in range(n):
            l_bound = max(prev_smaller[i], left_bit_limit[i])
            r_bound = min(next_smaller_or_equal[i], right_bit_limit[i])
            left_choices = i - l_bound
            right_choices = r_bound - i
            total_count += left_choices * right_choices

        return total_count

    # Official LeetCode method name alias
    countConsistentSubarrays = countConsistent


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = [
        ([5, 3, 1, 2], 6),
        ([1, 1, 1], 6),
        ([0], 1),
    ]

    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = sol.countConsistent(nums)
        assert result == expected, f"Test {idx} failed: expected {expected}, got {result}"
        print(f"Test case {idx}: nums={nums} -> result={result} (PASS)")

    print("\nAll test cases passed successfully!")