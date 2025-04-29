# ===== Sliding Window Practice Scaffold =====

# 1. Maximum Sum of Subarray of Size K
def max_sum_subarray_of_size_k(nums, k):
    # TODO: Sliding window of fixed size
    return 0

def test_max_sum_subarray_of_size_k():
    print(max_sum_subarray_of_size_k([2,1,5,1,3,2], 3))  # Expected: 9
    print(max_sum_subarray_of_size_k([2,3,4,1,5], 2))    # Expected: 7


# 2. Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    # TODO: Sliding window with hashmap
    return 0

def test_length_of_longest_substring():
    print(length_of_longest_substring("abcabcbb"))  # Expected: 3
    print(length_of_longest_substring("bbbbb"))    # Expected: 1
    print(length_of_longest_substring("pwwkew"))   # Expected: 3


# 3. Longest Substring with At Most K Distinct Characters
def longest_substring_k_distinct(s, k):
    # TODO: Variable sliding window with character count
    return 0

def test_longest_substring_k_distinct():
    print(longest_substring_k_distinct("eceba", 2))  # Expected: 3
    print(longest_substring_k_distinct("aa", 1))     # Expected: 2


# 4. Minimum Size Subarray Sum
def min_subarray_len(target, nums):
    # TODO: Shrinking sliding window
    return 0

def test_min_subarray_len():
    print(min_subarray_len(7, [2,3,1,2,4,3]))  # Expected: 2
    print(min_subarray_len(15, [1,2,3,4,5]))   # Expected: 5


# 5. Find All Anagrams in a String
def find_anagrams(s, p):
    # TODO: Sliding window with hashmap comparison
    return []

def test_find_anagrams():
    print(find_anagrams("cbaebabacd", "abc"))  # Expected: [0,6]
    print(find_anagrams("abab", "ab"))         # Expected: [0,1,2]


# 6. Minimum Window Substring
def min_window(s, t):
    # TODO: Hard sliding window with frequency count
    return ""

def test_min_window():
    print(min_window("ADOBECODEBANC", "ABC"))  # Expected: "BANC"
    print(min_window("a", "a"))                # Expected: "a"


# 7. Sliding Window Maximum (Using Deque)
def max_sliding_window(nums, k):
    # TODO: Monotonic deque to keep maximum at front
    return []

def test_max_sliding_window():
    print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # Expected: [3,3,5,5,6,7]
    print(max_sliding_window([1], 1))                  # Expected: [1]


# Run all tests
if __name__ == "__main__":
    test_max_sum_subarray_of_size_k()
    test_length_of_longest_substring()
    test_longest_substring_k_distinct()
    test_min_subarray_len()
    test_find_anagrams()
    test_min_window()
    test_max_sliding_window()
