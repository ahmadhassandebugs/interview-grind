# 🔁 Common Patterns: Two Pointers & Sliding Window

---

## ✅ Two Pointers

### 1. Opposite Ends
- **Idea**: One pointer at start, one at end; move inward based on condition.
- **Used for**: Searching pairs, checking symmetry, sorted arrays.
- **Examples**:
  - Two Sum II (sorted) — Leetcode 167
  - Valid Palindrome — Leetcode 125
  - Container With Most Water — Leetcode 11

---

### 2. Same Direction (Slow & Fast Pointers)
- **Idea**: Both pointers move right; one lags or advances based on logic.
- **Used for**: Removing duplicates, reordering, gaps.
- **Examples**:
  - Remove Duplicates from Sorted Array — Leetcode 26
  - Move Zeroes — Leetcode 283
  - Linked List Cycle Detection — Leetcode 141

---

### 3. Merge Style
- **Idea**: Traverse two arrays/lists like merge sort.
- **Used for**: Sorted data combination, interval problems.
- **Examples**:
  - Merge Two Sorted Lists — Leetcode 21
  - Merge Intervals — Leetcode 56
  - Intersection of Two Arrays II — Leetcode 350

---

### 4. Partition-Based
- **Idea**: Rearranging in-place using pointer(s) to partition segments.
- **Used for**: Dutch National Flag, QuickSort, value-based separation.
- **Examples**:
  - Sort Colors — Leetcode 75
  - Partition List — Leetcode 86
  - QuickSort Partition Logic

---

### 5. Subsequence Match
- **Idea**: Traverse two sequences and match characters in order.
- **Used for**: String/array pattern matching.
- **Examples**:
  - Is Subsequence — Leetcode 392
  - Longest Common Subsequence (DP + pointers)
  - Minimum Window Subsequence — Leetcode 727

---

## 📏 Sliding Window

### 1. Fixed Size Window
- **Idea**: Window of size `k`, slide right.
- **Used for**: Max/min/avg sum in k-length segment.
- **Examples**:
  - Maximum Average Subarray I — Leetcode 643
  - Max Consecutive Ones III — Leetcode 1004

---

### 2. Variable Size Window
- **Idea**: Expand right pointer until valid, then shrink left.
- **Used for**: Longest subarray/substring problems.
- **Examples**:
  - Longest Substring Without Repeating Characters — Leetcode 3
  - Longest Substring with At Most K Distinct Chars — Leetcode 340
  - Minimum Size Subarray Sum — Leetcode 209

---

### 3. Sliding Window with Hash Map
- **Idea**: Track character/frequency counts to find match windows.
- **Used for**: Anagrams, substrings, matching multisets.
- **Examples**:
  - Find All Anagrams in a String — Leetcode 438
  - Minimum Window Substring — Leetcode 76
  - Permutation in String — Leetcode 567

---

### 4. Sliding Window with Deque
- **Idea**: Use deque to maintain monotonic properties (min/max).
- **Used for**: Track window max/min in O(n).
- **Examples**:
  - Sliding Window Maximum — Leetcode 239
  - Shortest Subarray with Sum at Least K — Leetcode 862 (uses deque)

---

## 🧠 Summary: When to Use What?

| Problem Type | Strategy |
|--------------|----------|
| Pair sum / palindrome check | Two pointers (opposite ends) |
| Remove elements / merge lists | Two pointers (same direction) |
| Fixed segment operations | Sliding window (fixed) |
| Longest/shortest dynamic subarray | Sliding window (variable) |
| Match counts / frequency | Sliding window with hashmap |
| Track max/min in window | Sliding window with deque |

---
