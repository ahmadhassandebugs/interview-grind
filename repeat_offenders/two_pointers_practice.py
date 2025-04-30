# ===== Two Pointers Practice Scaffold =====

# 1. Two Sum II (Input array is sorted)
def two_sum_sorted(nums, target):
    # TODO: Implement two pointers from both ends
    pass

def test_two_sum_sorted():
    print(two_sum_sorted([2, 7, 11, 15], 9))  # Expected: [1, 2]
    print(two_sum_sorted([1, 2, 3, 4, 4, 9, 56, 90], 8))  # Expected: [4, 5]
    print(two_sum_sorted([1, 3, 4, 5, 7, 10, 11], 9))  # Expected: [3, 4]


# 2. Valid Palindrome (alphanumeric only)
def is_palindrome(s):
    # TODO: Skip non-alphanum and compare with two pointers
    pass

def test_is_palindrome():
    print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected: True
    print(is_palindrome("race a car"))  # Expected: False
    print(is_palindrome(""))  # Expected: True


# 3. Container With Most Water
def max_area(height):
    # TODO: Two pointers to find max area
    pass

def test_max_area():
    print(max_area([1,8,6,2,5,4,8,3,7]))  # Expected: 49
    print(max_area([1,1]))  # Expected: 1
    print(max_area([4,3,2,1,4]))  # Expected: 16


# 4. Remove Duplicates from Sorted Array (In-place)
# [1,1,2,3,3]
# l is where the new unique number goes
# r is the current number
# copy r number if it's different from l-1 and move l and r
# else, move r to find a new number
def remove_duplicates(nums):
    # TODO: Modify array in-place, return new length
    pass

def test_remove_duplicates():
    nums = [1,1,2]
    k = remove_duplicates(nums)
    print(k, nums[:k])  # Expected: 2, [1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = remove_duplicates(nums)
    print(k, nums[:k])  # Expected: 5, [0,1,2,3,4]


# 5. Move Zeroes (In-place)
# same approach as above but with zeros instead of same number condition
def move_zeroes(nums):
    # TODO: Move non-zeroes forward, zeroes to end
    pass

def test_move_zeroes():
    nums = [0,1,0,3,12]
    move_zeroes(nums)
    print(nums)  # Expected: [1,3,12,0,0]
    nums = [0,0,1]
    move_zeroes(nums)
    print(nums)  # Expected: [1,0,0]


# 6. Merge Two Sorted Arrays (A has enough space at end)
# start from the end
def merge_sorted_arrays(nums1, m, nums2, n):
    # TODO: Merge in-place starting from the end
    pass

def test_merge_sorted_arrays():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    merge_sorted_arrays(nums1, 3, nums2, 3)
    print(nums1)  # Expected: [1,2,2,3,5,6]
    nums1 = [4,5,6,0,0,0]
    nums2 = [1,2,3]
    merge_sorted_arrays(nums1, 3, nums2, 3)
    print(nums1)  # Expected: [1,2,3,4,5,6]
    nums1 = [1,2,3,0,0,0]
    nums2 = [4,5,6]
    merge_sorted_arrays(nums1, 3, nums2, 3)
    print(nums1)  # Expected: [1,2,3,4,5,6]


# 7. Sort Colors (Dutch National Flag)
def sort_colors(nums):
    # TODO: Three pointers for 0s, 1s, and 2s
    pass

def test_sort_colors():
    nums = [2,0,2,1,1,0]
    sort_colors(nums)
    print(nums)  # Expected: [0,0,1,1,2,2]
    nums = [2,0,1]
    sort_colors(nums)
    print(nums)  # Expected: [0,1,2]


# 8. Is Subsequence
def is_subsequence(s, t):
    # TODO: Traverse both with two pointers
    pass

def test_is_subsequence():
    print(is_subsequence("abc", "ahbgdc"))  # Expected: True
    print(is_subsequence("axc", "ahbgdc"))  # Expected: False
    print(is_subsequence("", "ahbgdc"))  # Expected: True


# Run all tests
if __name__ == "__main__":
    test_two_sum_sorted()
    test_is_palindrome()
    test_max_area()
    test_remove_duplicates()
    test_move_zeroes()
    test_merge_sorted_arrays()
    test_sort_colors()
    test_is_subsequence()
