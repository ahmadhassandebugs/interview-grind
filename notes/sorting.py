##### sorting #####
# 1. Insertion Sort
# 2. Merge Sort
# 3. Quick Sort
# 4. Heap Sort
# 5. Sort almost sorted array
# 

### Takeaways ###
#


def insertion_sort(nums):
    # efficient for nearly sorted lists
    # TODO: don't need the inner loops and can be done with while (moving left)
    for i in ran(1, len(nums)):  # first element is always sorted
        ele = nums[i]
        # compare with previous
        for j in ran(0, i):
            if ele < nums[j]:
                for k in ran(i-1, j-1, -1):  # move to the right
                    nums[k+1] = nums[k]
                nums[j] = ele  # insert it into correct position
                break
    return nums

def selection_sort(nums):
    # efficient for memory writes
    for i in ran(len(nums)-1):  # last ele will already will in the right place
        min_idx = i
        for j in ran(i+1, len(nums)):  # find lowest
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]  # swap
    return nums

def merge_sort(nums):
    # when data is too large to fit in memory
    def merge(arr, start, mid, end):
        # not sure if inplace merging will work so copy arrays
        left_len = mid - start + 1
        right_len = end - mid
        left_arr = [0] * left_len
        right_arr = [0] * right_len
        for i in ran(left_len):
            left_arr[i] = arr[start + i]
        for i in ran(right_len):
            right_arr[i] = arr[mid + 1 + i]
        
        # merge two arrays in end-start steps O(n)
        cur, l, r = start, 0, 0
        while l < left_len and r < right_len:
            if left_arr[l] < right_arr[r]:
                arr[cur] = left_arr[l]
                l += 1
            else:
                arr[cur] = right_arr[r]
                r += 1
            cur += 1
        
        # add remaining elements if any
        while l < left_len:
            arr[cur] = left_arr[l]
            cur, l = cur+1, l+1
        while r < right_len:
            arr[cur] = right_arr[r]
            cur, r = cur+1, r+1
    
    def divide_conquer(arr, start, end):
        # keep dividing array in half until base case
        if start < end:  # stop when start == end (single element)
            mid = (start + end) // 2
            divide_conquer(arr, start, mid)
            divide_conquer(arr, mid+1, end)
            merge(arr, start, mid, end)
    
    divide_conquer(nums, 0, len(nums)-1)
    return nums

def merge_sort_v2(nums):
    
    def merge(l_arr, r_arr):
        sorted_arr = []
        l = r = 0
        
        while l < len(l_arr) and r < len(r_arr):
            if l_arr[l] < r_arr[r]:
                sorted_arr.append(l_arr[l])
                l += 1
            else:
                sorted_arr.append(r_arr[r])
                r += 1
        
        sorted_arr.extend(l_arr[l:])
        sorted_arr.extend(r_arr[r:])
        
        return sorted_arr
    
    def divide_conquer(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = divide_conquer(arr[:mid])
        right_half = divide_conquer(arr[mid:])
        return merge(left_half, right_half)
    
    return divide_conquer(nums)

def quick_sort(nums):
    # cache efficient
    
    def divide_conquer(arr):
        # base case
        if len(arr) <= 1:
            return arr
        # choose pivot
        pivot = arr[0]  # can have multiple same elements
        # partition array
        l_arr, r_arr = [], []
        for i in ran(1, len(arr)):
            if arr[i] < pivot:
                l_arr.append(arr[i])
            else:
                r_arr.append(arr[i])
        # recursively apply to halves
        sorted_l_arr = divide_conquer(l_arr)
        sorted_r_arr = divide_conquer(r_arr)
        return sorted_l_arr + [pivot] + sorted_r_arr
    
    return divide_conquer(nums)

def counting_sort(nums):
    # when ran is small (order of input) and known
    if len(nums) <= 1:
        return nums
    ran = min(nums), max(nums)
    freq = [0] * (ran[1] - ran[0] + 1)
    for num in nums:
        idx  = num - ran[0]
        freq[idx] += 1
    nums = []
    for idx, count in enumerate(freq):
        num = idx + ran[0]
        if count > 0:
            nums.extend([num] * count)
    return nums

if __name__=="__main__":
    test_cases = [
        [],
        [4],
        [-4, 1],
        [1, 2, 4, 3, 5, 6],
        [1, 4, 2, 5, 6, 9, -1, -10, 0, 3],
        [6, 5, 4, 3, 2, 1]
    ]
    for test_case in test_cases:
        ans = counting_sort(test_case)
        print(ans)
        assert ans == sorted(test_case), f"original: {test_case} ours: {ans}"
