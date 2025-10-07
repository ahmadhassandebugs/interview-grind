"""

"""

# --------------------------------------------------------------------
# 1. Fibonacci Number / Climbing Stairs (1D DP Basics)
# --------------------------------------------------------------------

def fibonacci_memo(n: int, memo: dict = None) -> int:
    """
    Calculates the nth Fibonacci number using memoization (Top-Down DP).
    F(n) = F(n-1) + F(n-2).
    """
    if memo is None:
        memo = {}
    
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    
    # --- SOLUTION LOGIC GOES HERE ---
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    # --------------------------------
    return memo[n]

def climb_stairs(n: int) -> int:
    """
    Finds the number of distinct ways to climb to the top of n stairs, 
    where you can take 1 or 2 steps at a time (Tabulation - Bottom-Up DP).
    """
    if n <= 2:
        return n
    
    # DP array: dp[i] is the number of ways to reach step i.
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    # --- SOLUTION LOGIC GOES HERE ---
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # --------------------------------
        
    return dp[n]

# --------------------------------------------------------------------
# 2. House Robber (1D DP Optimization)
# --------------------------------------------------------------------

def house_robber(nums: list[int]) -> int:
    """
    Finds the maximum amount of money that can be robbed without robbing 
    two adjacent houses. DP[i] = max(DP[i-1], DP[i-2] + nums[i]).
    Space-optimized implementation (O(1) space).
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    # --- SOLUTION LOGIC GOES HERE ---
    for i in range(2, n):
        current_max = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current_max
    # --------------------------------
        
    return prev1

# --------------------------------------------------------------------
# 3. Longest Increasing Subsequence (LIS - 1D Sequence DP)
# --------------------------------------------------------------------

def longest_increasing_subsequence(nums: list[int]) -> int:
    """
    Finds the length of the longest increasing subsequence in an array.
    DP[i] = 1 + max(DP[j]) for all j < i where nums[j] < nums[i].
    (O(n^2) DP solution)
    """
    n = len(nums)
    if n == 0:
        return 0
    
    # dp[i] stores the length of the LIS ending at index i.
    dp = [1] * n
    max_len = 1
    
    # --- SOLUTION LOGIC GOES HERE ---
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])
    # --------------------------------
        
    return max_len

# --------------------------------------------------------------------
# 4. Longest Common Subsequence (LCS - 2D String DP)
# --------------------------------------------------------------------

def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Finds the length of the longest common subsequence between two strings.
    2D DP table: DP[i][j] max LCS for text1[0..i-1] and text2[0..j-1].
    """
    m, n = len(text1), len(text2)
    
    # Initialize DP table (m+1 rows, n+1 columns)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # --- SOLUTION LOGIC GOES HERE ---
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # --------------------------------
                
    return dp[m][n]

# --------------------------------------------------------------------
# 5. Minimum Path Sum (2D Grid DP)
# --------------------------------------------------------------------

def minimum_path_sum(grid: list[list[int]]) -> int:
    """
    Finds the minimum path sum from top-left to bottom-right of a grid, 
    moving only down or right. Uses the grid for in-place DP.
    DP[i][j] = grid[i][j] + min(DP[i-1][j], DP[i][j-1])
    """
    m, n = len(grid), len(grid[0])
    
    # --- SOLUTION LOGIC GOES HERE ---
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    # --------------------------------
                
    return grid[m - 1][n - 1]

# --------------------------------------------------------------------
# 6. Coin Change (Unbounded Knapsack)
# --------------------------------------------------------------------

def coin_change_min_coins(coins: list[int], amount: int) -> int:
    """
    Calculates the fewest number of coins needed to make up a given amount.
    Unbounded Knapsack-style DP. DP[a] = min(DP[a - coin]) + 1.
    """
    # dp[i] is the minimum number of coins to make amount i.
    impossible = amount + 1
    dp = [impossible] * (amount + 1)
    dp[0] = 0 # 0 coins for amount 0
    
    # --- SOLUTION LOGIC GOES HERE ---
    for a in range(1, amount + 1):
        for coin in coins:
            if a >= coin:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    # --------------------------------
                
    return dp[amount] if dp[amount] != impossible else -1

# --------------------------------------------------------------------
# 7. 0/1 Knapsack Problem (0/1 Knapsack)
# --------------------------------------------------------------------

def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Finds the maximum value that can be obtained by filling a knapsack 
    where each item can be used at most once.
    Space-optimized 1D DP: DP[w] stores max value for capacity w.
    """
    n = len(weights)
    
    # dp[w] stores the max value for capacity w
    dp = [0] * (capacity + 1)
    
    # --- SOLUTION LOGIC GOES HERE ---
    for i in range(n): # Iterate through items
        weight = weights[i]
        value = values[i]
        
        # Iterate through capacity *backwards*
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], value + dp[w - weight])
    # --------------------------------
            
    return dp[capacity]

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
