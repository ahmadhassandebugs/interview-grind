# filename: dp_practice_scaffold.py

# ====================================================================
# DYNAMIC PROGRAMMING PRACTICE SET (7 Core Problems)
# ====================================================================

# --------------------------------------------------------------------
# 1. Fibonacci Number / Climbing Stairs (1D DP Basics)
# --------------------------------------------------------------------

def fibonacci_memo(n: int, memo: dict = None) -> int:
    pass

def climb_stairs(n: int) -> int:
    pass

# --------------------------------------------------------------------
# 2. House Robber (1D DP Optimization)
# --------------------------------------------------------------------

def house_robber(nums: list[int]) -> int:
    pass

# --------------------------------------------------------------------
# 3. Longest Increasing Subsequence (LIS - 1D Sequence DP)
# --------------------------------------------------------------------

def longest_increasing_subsequence(nums: list[int]) -> int:
    pass

# --------------------------------------------------------------------
# 4. Longest Common Subsequence (LCS - 2D String DP)
# --------------------------------------------------------------------

def longest_common_subsequence(text1: str, text2: str) -> int:
    pass

# --------------------------------------------------------------------
# 5. Minimum Path Sum (2D Grid DP)
# --------------------------------------------------------------------

def minimum_path_sum(grid: list[list[int]]) -> int:
    pass

# --------------------------------------------------------------------
# 6. Coin Change (Unbounded Knapsack)
# --------------------------------------------------------------------

def coin_change_min_coins(coins: list[int], amount: int) -> int:
    pass

# --------------------------------------------------------------------
# 7. 0/1 Knapsack Problem (0/1 Knapsack)
# --------------------------------------------------------------------

def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    pass

# ====================================================================
# TEST CASES
# ====================================================================

print("--- 1. Fibonacci / Climbing Stairs ---")
print(f"Fib(6) (Memo): {fibonacci_memo(6)}")      # Expected: 8
print(f"Climbing Stairs(4): {climb_stairs(4)}")   # Expected: 5

print("\n--- 2. House Robber ---")
print(f"House Robber [2,7,9,3,1]: {house_robber([2, 7, 9, 3, 1])}") # Expected: 12

print("\n--- 3. Longest Increasing Subsequence ---")
print(f"LIS [10,9,2,5,3,7,101,18]: {longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])}") # Expected: 4

print("\n--- 4. Longest Common Subsequence ---")
print(f"LCS (abcde, ace): {longest_common_subsequence('abcde', 'ace')}") # Expected: 3

print("\n--- 5. Minimum Path Sum ---")
# Must create a new list for the test since the function modifies the grid in-place
grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]] 
print(f"Min Path Sum: {minimum_path_sum(grid1)}") # Expected: 7

print("\n--- 6. Coin Change (Minimum Coins) ---")
print(f"Coin Change [1,2,5] for 11: {coin_change_min_coins([1, 2, 5], 11)}") # Expected: 3
print(f"Coin Change [2] for 3: {coin_change_min_coins([2], 3)}")             # Expected: -1

print("\n--- 7. 0/1 Knapsack Problem ---")
weights_list = [2, 3, 4, 5]
values_list = [3, 4, 5, 6]
knapsack_capacity = 5
print(f"0/1 Knapsack Max Value: {knapsack_01(weights_list, values_list, knapsack_capacity)}") # Expected: 7
