# LeetCode Weekly Contest 528

This folder contains Python solutions with local test runners for all problems from **LeetCode Weekly Contest 528**.

## Problems Summary

| # | Title | Difficulty | Solution File | Key Topics / Approach |
|---|-------|------------|---------------|------------------------|
| Q1 | [Count Consistent Subarrays I](https://leetcode.com/problems/count-consistent-subarrays-i/) | Easy | [`q1_count_consistent_subarrays_i.py`](q1_count_consistent_subarrays_i.py) | Brute Force / Running Bitwise AND, $O(N^2)$ |
| Q2 | [Maximize Score After Zeroing Subtrees](https://leetcode.com/problems/maximize-score-after-zeroing-subtrees/) | Medium | [`q2_maximize_score_after_zeroing_subtrees.py`](q2_maximize_score_after_zeroing_subtrees.py) | Tree DFS / Greedy Dynamic Programming, $O(N)$ |
| Q3 | [Game of Divisible Sums](https://leetcode.com/problems/game-of-divisible-sums/) | Medium / Hard | [`q3_game_of_divisible_sums.py`](q3_game_of_divisible_sums.py) | Game Theory / Minimax Memoization DP, $O(N)$ |
| Q4 | [Count Consistent Subarrays II](https://leetcode.com/problems/count-consistent-subarrays-ii/) | Hard | [`q4_count_consistent_subarrays_ii.py`](q4_count_consistent_subarrays_ii.py) | Monotonic Stack + Bitwise Boundary Tracking, $O(21 \cdot N) \approx O(N)$ |

---

## Running the Solutions

Each solution file includes an `if __name__ == "__main__":` block with LeetCode example test cases and assertions:

```bash
python contest_528/q1_count_consistent_subarrays_i.py
python contest_528/q2_maximize_score_after_zeroing_subtrees.py
python contest_528/q3_game_of_divisible_sums.py
python contest_528/q4_count_consistent_subarrays_ii.py
```
