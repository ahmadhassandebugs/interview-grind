# filename: dp_practice_scaffold.py

# ====================================================================
# DYNAMIC PROGRAMMING PRACTICE SET (7 Core Problems)
# ====================================================================

# --------------------------------------------------------------------
# 1. Fibonacci Number / Climbing Stairs
# --------------------------------------------------------------------

def fibonacci_memo(n: int, memo: dict = None) -> int:
    pass

def climb_stairs(n: int) -> int:
    pass

# --------------------------------------------------------------------
# 2. House Robber
# --------------------------------------------------------------------

def house_robber(nums: list[int]) -> int:
    pass

# --------------------------------------------------------------------
# 3. Longest Increasing Subsequence
# --------------------------------------------------------------------

def longest_increasing_subsequence(nums: list[int]) -> int:
    pass

# --------------------------------------------------------------------
# 4. Longest Common Subsequence
# --------------------------------------------------------------------

def longest_common_subsequence(text1: str, text2: str) -> int:
    pass

# --------------------------------------------------------------------
# 5. Minimum Path Sum
# --------------------------------------------------------------------

def minimum_path_sum(grid: list[list[int]]) -> int:
    pass

# --------------------------------------------------------------------
# 6. Coin Change
# --------------------------------------------------------------------

def coin_change_min_coins(coins: list[int], amount: int) -> int:
    pass

# --------------------------------------------------------------------
# 7. 0/1 Knapsack Problem
# --------------------------------------------------------------------

def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    pass


# ====================================================================
# TEST CASES
# ====================================================================

def run_tests():
    """Runs the extensive test suite."""

    print("--- 1a. Fibonacci Number (Standard Sequence) ---")
    fib_tests = [
        {"n": 0, "expected": 0, "reason": "Base case: F(0)"},
        {"n": 1, "expected": 1, "reason": "Base case: F(1)"},
        {"n": 2, "expected": 1, "reason": "First calculation: 1 + 0"},
        {"n": 6, "expected": 8, "reason": "Standard case"},
        {"n": 10, "expected": 55, "reason": "Standard case"},
        {"n": 40, "expected": 102334155, "reason": "Larger input to test performance"},
    ]

    for test in fib_tests:
        n, expected = test["n"], test["expected"]        
        res_memo = fibonacci_memo(n)
        pass_memo = res_memo == expected
        print(f"Input: n={n}, Output: {res_memo}, Expected: {expected} -> {'PASS' if pass_memo else 'FAIL'}")

    # --- 1. Climbing Stairs ---
    print("\n--- 1. Climbing Stairs ---")
    climb_stairs_tests = [
        {"n": 0, "expected": 1, "reason": "Base case: 0 stairs"},
        {"n": 1, "expected": 1, "reason": "Base case: 1 stair"},
        {"n": 2, "expected": 2, "reason": "Standard case"},
        {"n": 5, "expected": 8, "reason": "Standard case"},
        {"n": 45, "expected": 1836311903, "reason": "Large input"},
    ]
    for test in climb_stairs_tests:
        n, expected = test["n"], test["expected"]
        result = climb_stairs(n)
        print(f"Input: n={n}, Output: {result}, Expected: {expected} -> {'PASS' if result == expected else 'FAIL'}")

    # --- 2. House Robber ---
    print("\n--- 2. House Robber ---")
    house_robber_tests = [
        {"nums": [], "expected": 0, "reason": "Edge case: No houses"},
        {"nums": [10], "expected": 10, "reason": "Edge case: One house"},
        {"nums": [10, 20], "expected": 20, "reason": "Two houses, take larger"},
        {"nums": [2, 7, 9, 3, 1], "expected": 12, "reason": "Standard case (2+9+1)"},
        {"nums": [6, 7, 1, 30, 8, 2, 4], "expected": 41, "reason": "Longer list (7+30+4)"},
        {"nums": [10, 1, 1, 10], "expected": 20, "reason": "Rob first and last possible (10+10)"},
        {"nums": [0, 0, 0, 0], "expected": 0, "reason": "All zero values"},
    ]
    for test in house_robber_tests:
        nums, expected = test["nums"], test["expected"]
        result = house_robber(nums)
        print(f"Input: {nums}, Output: {result}, Expected: {expected} -> {'PASS' if result == expected else 'FAIL'}")

    # --- 3. Longest Increasing Subsequence ---
    print("\n--- 3. Longest Increasing Subsequence ---")
    lis_tests = [
        {"nums": [], "expected": 0, "reason": "Edge case: Empty array"},
        {"nums": [5], "expected": 1, "reason": "Edge case: Single element"},
        {"nums": [10, 9, 2, 5, 3, 7, 101, 18], "expected": 4, "reason": "Standard case [2,3,7,101]"},
        {"nums": [1, 2, 3, 4, 5], "expected": 5, "reason": "Already sorted"},
        {"nums": [5, 4, 3, 2, 1], "expected": 1, "reason": "Reverse sorted"},
        {"nums": [7, 7, 7, 7], "expected": 1, "reason": "All elements same"},
        {"nums": [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], "expected": 6, "reason": "Complex case"},
    ]
    for test in lis_tests:
        nums, expected = test["nums"], test["expected"]
        result = longest_increasing_subsequence(nums)
        print(f"Input: {nums}, Output: {result}, Expected: {expected} -> {'PASS' if result == expected else 'FAIL'}")

    # --- 4. Longest Common Subsequence ---
    print("\n--- 4. Longest Common Subsequence ---")
    lcs_tests = [
        {"t1": "abcde", "t2": "ace", "expected": 3, "reason": "Standard case ('ace')"},
        {"t1": "", "t2": "abcde", "expected": 0, "reason": "Edge case: one empty"},
        {"t1": "abcde", "t2": "", "expected": 0, "reason": "Edge case: one empty"},
        {"t1": "", "t2": "", "expected": 0, "reason": "Edge case: both empty"},
        {"t1": "abc", "t2": "def", "expected": 0, "reason": "No common characters"},
        {"t1": "AGGTAB", "t2": "GXTXAYB", "expected": 4, "reason": "Classic example ('GTAB')"},
        {"t1": "banana", "t2": "atana", "expected": 4, "reason": "Overlapping chars ('atana')"},
        {"t1": "aaaa", "t2": "aa", "expected": 2, "reason": "Repeated chars"},
    ]
    for test in lcs_tests:
        t1, t2, expected = test["t1"], test["t2"], test["expected"]
        result = longest_common_subsequence(t1, t2)
        print(f"Input: ('{t1}', '{t2}'), Output: {result}, Expected: {expected} -> {'PASS' if result == expected else 'FAIL'}")

    # --- 5. Minimum Path Sum ---
    print("\n--- 5. Minimum Path Sum ---")
    min_path_tests = [
        {"grid": [[1, 3, 1], [1, 5, 1], [4, 2, 1]], "expected": 7, "reason": "Standard case"},
        {"grid": [[10]], "expected": 10, "reason": "Edge case: 1x1 grid"},
        {"grid": [[1, 2, 3, 4]], "expected": 10, "reason": "Edge case: 1xN grid"},
        {"grid": [[1], [2], [3], [4]], "expected": 10, "reason": "Edge case: Nx1 grid"},
        {"grid": [[1, 10, 1], [10, 1, 1], [1, 10, 1]], "expected": 14, "reason": "Non-greedy path is optimal"},
    ]
    import copy
    for test in min_path_tests:
        # Create a deep copy since the function modifies the grid in-place
        grid, expected = copy.deepcopy(test["grid"]), test["expected"]
        result = minimum_path_sum(grid)
        print(f"Input: {test['grid']}, Output: {result}, Expected: {expected} -> {'PASS' if result == expected else 'FAIL'}")

    # --- 6. Coin Change (Minimum Coins) ---
    print("\n--- 6. Coin Change (Minimum Coins) ---")
    coin_change_tests = [
        {"coins": [1, 2, 5], "amount": 11, "expected": 3, "reason": "Standard case (5+5+1)"},
        {"coins": [1, 2, 5], "amount": 0, "expected": 0, "reason": "Edge case: amount is 0"},
        {"coins": [2], "amount": 3, "expected": -1, "reason": "Impossible case"},
        {"coins": [3, 5], "amount": 7, "expected": -1, "reason": "Impossible case"},
        {"coins": [1, 3, 4], "amount": 6, "expected": 2, "reason": "Greedy approach fails (3+3 is better than 4+1+1)"},
        {"coins": [186, 419, 83, 408], "amount": 6249, "expected": 20, "reason": "Complex case"},
    ]
    for test in coin_change_tests:
        coins, amount, expected = test["coins"], test["amount"], test["expected"]
        result = coin_change_min_coins(coins, amount)
        print(f"Input: ({coins}, {amount}), Output: {result}, Expected: {expected} -> {'PASS' if result == expected else 'FAIL'}")

    # --- 7. 0/1 Knapsack Problem ---
    print("\n--- 7. 0/1 Knapsack Problem ---")
    knapsack_tests = [
        {"w": [2, 3, 4, 5], "v": [3, 4, 5, 6], "cap": 5, "expected": 7, "reason": "Standard case (w:2+3, v:3+4)"},
        {"w": [], "v": [], "cap": 10, "expected": 0, "reason": "Edge case: no items"},
        {"w": [2, 3], "v": [10, 15], "cap": 0, "expected": 0, "reason": "Edge case: zero capacity"},
        {"w": [10], "v": [100], "cap": 5, "expected": 0, "reason": "Item too heavy"},
        {"w": [1, 2, 3], "v": [10, 20, 30], "cap": 6, "expected": 60, "reason": "All items fit"},
        {"w": [5, 4, 6, 3], "v": [10, 40, 30, 50], "cap": 10, "expected": 90, "reason": "Tricky case (w:4+3, v:40+50)"},
    ]
    for test in knapsack_tests:
        w, v, cap, expected = test["w"], test["v"], test["cap"], test["expected"]
        result = knapsack_01(w, v, cap)
        print(f"Input: (w:{w}, v:{v}, cap:{cap}), Output: {result}, Expected: {expected} -> {'PASS' if result == expected else 'FAIL'}")


if __name__ == "__main__":
    run_tests()
