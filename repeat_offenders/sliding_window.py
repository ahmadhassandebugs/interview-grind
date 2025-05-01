from collections import Counter
# ===== Sliding Window Practice Scaffold =====

# 1. Maximum Sum of Subarray of Size K
def max_sum_subarray_of_size_k(nums, k):
    l, max_sum = 0, 0
    while l <= len(nums) - k:
        if sum(nums[l:l+k]) > max_sum: max_sum = sum(nums[l:l+k])
        l += 1
    return max_sum

def test_max_sum_subarray_of_size_k():
    print(max_sum_subarray_of_size_k([2,1,5,1,3,2], 3))  # Expected: 9
    print(max_sum_subarray_of_size_k([2,3,4,1,5], 2))    # Expected: 7


# 2. Longest Substring Without Repeating Characters
# l and r ptrs
# keep incrementing r
# if not unique remove repeating cha and move l
#   might be in the middle so have to move multiple steps
def length_of_longest_substring(s):
    ch_dict, longest_str = {}, 0
    l, r = 0, 0
    while r < len(s):
        while s[r] in ch_dict:
            del ch_dict[s[l]]
            l += 1
        ch_dict[s[r]] = 1
        if r - l + 1 > longest_str: longest_str = r - l + 1
        r += 1
    return longest_str

def test_length_of_longest_substring():
    print(length_of_longest_substring("abcabcbb"))  # Expected: 3
    print(length_of_longest_substring("bbbbb"))    # Expected: 1
    print(length_of_longest_substring("pwwkew"))   # Expected: 3


# 3. Longest Substring with At Most K Distinct Characters
# l and r ptrs
# keep incrementing r and check for longest
# if len(ch_dict) == k and ch not in ch_dict
#   move l till len(ch_dict) < k and update ch_dict
def longest_substring_k_distinct(s, k):
    c, longest_str = Counter(), 0
    l, r = 0, 0
    while r < len(s):
        while s[r] not in c and len(c) >= k:
            c[s[l]] -= 1
            if c[s[l]] == 0: del c[s[l]]
            l += 1
        c[s[r]] += 1
        if r - l + 1 > longest_str: longest_str = r - l + 1
        r += 1
    return longest_str

def test_longest_substring_k_distinct():
    print(longest_substring_k_distinct("eceba", 2))  # Expected: 3
    print(longest_substring_k_distinct("aa", 1))     # Expected: 2


# 4. Minimum Size Subarray Sum
# l and r ptrs
# if sum equal, update min_len
# if sum small, move r
# if sum large, move l
def min_subarray_len(target, nums):
    l, r = 0, 1
    min_len = len(nums)
    while r <= len(nums):
        if sum(nums[l:r]) == target:
            if r - l < min_len: min_len = r - l
            r += 1
            l += 1
        elif sum(nums[l:r]) < target: r += 1
        else: l += 1
    return min_len

def test_min_subarray_len():
    print(min_subarray_len(7, [2,3,1,2,4,3]))  # Expected: 2
    print(min_subarray_len(15, [1,2,3,4,5]))   # Expected: 5


# 5. Find All Anagrams in a String
def find_anagrams(s, p):
    c = Counter(p)
    answer = []
    l, p_len = 0, len(p)
    while l < len(s):
        if c == Counter(s[l:l+p_len]): answer.append(l)
        l += 1
    return answer

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
