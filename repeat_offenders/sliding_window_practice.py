# ===== Sliding Window Practice Scaffold =====

# 1. Maximum Sum of Subarray of Size K
def max_sum_subarray_of_size_k(nums, k):
    pass

def test_max_sum_subarray_of_size_k():
    print(max_sum_subarray_of_size_k([2,1,5,1,3,2], 3))  # Expected: 9
    print(max_sum_subarray_of_size_k([2,3,4,1,5], 2))    # Expected: 7


# 2. Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    pass

def test_length_of_longest_substring():
    print(length_of_longest_substring("abcabcbb"))  # Expected: 3
    print(length_of_longest_substring("bbbbb"))    # Expected: 1
    print(length_of_longest_substring("pwwkew"))   # Expected: 3


# 3. Longest Substring with At Most K Distinct Characters
def longest_substring_k_distinct(s, k):
    pass

def test_longest_substring_k_distinct():
    print(longest_substring_k_distinct("eceba", 2))  # Expected: 3
    print(longest_substring_k_distinct("aa", 1))     # Expected: 2


# 4. Minimum Size Subarray Sum
def min_subarray_len(target, nums):
    pass

def test_min_subarray_len():
    print(min_subarray_len(7, [2,3,1,2,4,3]))  # Expected: 2
    print(min_subarray_len(15, [1,2,3,4,5]))   # Expected: 5


# 5. Find All Anagrams in a String
def find_anagrams(s, p):
    pass

def test_find_anagrams():
    print(find_anagrams("cbaebabacd", "abc"))  # Expected: [0,6]
    print(find_anagrams("abab", "ab"))         # Expected: [0,1,2]

# Run all tests
if __name__ == "__main__":
    test_max_sum_subarray_of_size_k()
    test_length_of_longest_substring()
    test_longest_substring_k_distinct()
    test_min_subarray_len()
    test_find_anagrams()
