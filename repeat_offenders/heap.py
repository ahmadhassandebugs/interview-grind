# Notes:
# - You may use Python's heapq (min-heap). For max-heap, push negatives or use tuples.
# - Keep solutions O(n log k) / O(n log n) as appropriate.
# ------------------------------------------

from __future__ import annotations
from typing import List, Optional, Iterable, Tuple
import heapq
import unittest
from dataclasses import dataclass


# ---------------------------
# Level 1
# ---------------------------

def kth_largest(nums: List[int], k: int) -> int:
    """
    LeetCode #215: Kth Largest Element in an Array
    Return the kth largest element in the unsorted array.

    Constraints to consider:
      - 1 <= k <= len(nums)
      - nums can be large; aim for O(n log k) with a size-k min-heap.

    Examples:
      nums = [3,2,1,5,6,4], k=2 -> 5
      nums = [3,2,3,1,2,4,5,5,6], k=4 -> 4
    """
    # Brute-force: Go over all elements and find largest, then 2nd largest, ..., kth largest
    #              O(k.n) time; O(1) space
    # Use max-heap: Store all elements in a heap O(n); then, pop k elements O(k.logn)
    #              O(k.logn) time; O(n) space can be made O(k)
    
    heap = [-num for num in nums]
    heapq.heapify(heap)
    for _ in range(k - 1): heapq.heappop(heap)
    return -heapq.heappop(heap)


def last_stone_weight(stones: List[int]) -> int:
    """
    LeetCode #1046: Last Stone Weight
    Repeatedly smash the two heaviest stones; if unequal, push back the difference.
    Use a max-heap pattern (e.g., store negatives in heapq).

    Examples:
      stones = [2,7,4,1,8,1] -> 1
    """
    # Brute-force: Get 2 heaviest stones each time O(2.n); Destroy the stones
    #              Worst case (1 stone destroyed) Best case (both stones destroyed)
    #              O(n^2) time; O(1) space
    # Max-heap: Heapify O(n); Get two stones O(logn); Add one back or not O(logn)
    #              Worst Case O(n.logn) time; O(n) space
    heap = [-stone for stone in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        y, x = -heapq.heappop(heap), -heapq.heappop(heap)
        if x == y: continue
        else: heapq.heappush(heap, -(y - x))
    return -heap[0] if heap else 0

# ---------------------------
# Level 2
# ---------------------------

@dataclass
class ListNode:
    val: int
    next: Optional['ListNode'] = None


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    LeetCode #23: Merge k Sorted Lists
    Merge k increasing linked lists into one sorted list.

    Examples:
      Input: [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
    """
    # Brute-force: Find which list has the smallest element O(k)
    #              then, merge and repeat
    #              O(n.k)
    # Min-heap: Maintain a heap, pick smallest O(logk), attach to the
    #           new list, add next element to heap O(logk), repeat
    #              O(n.logk)
    heap = []
    dummy = curr = ListNode(0)

    for idx, head in enumerate(lists):
        if head: heap.append((head.val, idx))
    heapq.heapify(heap)
    
    while heap:
        _, l_idx = heapq.heappop(heap)
        curr.next = lists[l_idx]
        curr = curr.next
        if lists[l_idx].next:
            heapq.heappush(heap, (lists[l_idx].next.val, l_idx))
            lists[l_idx] = lists[l_idx].next
    
    return dummy.next


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    LeetCode #347: Top K Frequent Elements
    Return any ordering of the k most frequent elements.

    Example:
      nums = [1,1,1,2,2,3], k=2 -> [1,2]
    """
    # Brute-force: Use a frequency counter O(n); sort it O(nlogn)
    #              O(nlogn) time; O(n) space
    # Max-heap: Use a frequency counter O(n); heapify O(n); remove k O(k.logn)
    #              O(k.logn) time; O(n) space
    from collections import Counter
    freq_map = Counter(nums)
    heap = [(-val, key) for (key, val) in freq_map.items()]
    heapq.heapify(heap)
    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])
    return res


class MedianFinder:
    """
    LeetCode #295: Find Median from Data Stream
    Maintain two heaps:
      - max-heap (lower half)  -> use negatives with heapq
      - min-heap (upper half)

    Invariants:
      - len(lower) == len(upper) or len(lower) == len(upper) + 1
      - All elements in lower <= all elements in upper
    """
    # max-heap (lower half) median will be on top
    # min-heap (upper half) median will be on top
    # 1,2,3,4,5
    # max-heap: 1,2
    # min-heap: 4
    # equal elements
    #   new_ele <= max-heap (should be in lower half); just insert to max-heap
    #   new_ele >= min-heap (should be in upper half); move min-heap top to max-heap and insert into min-heap
    #   max-heap < new_ele < min-heap (should be in lower half); just insert to max-heap
    # unequal elements
    #   new_ele <= max-heap (should be in lower half); move max-heap to min-heap and insert into max-heap
    #   new_ele >= min-heap (should be in upper half); just insert it to min-heap
    #   max-heap < new_ele < min-heap (should be in upper half); just insert it to min-heap

    def __init__(self) -> None:
        self.lower = []  # max-heap via negatives
        self.upper = []  # min-heap

    def addNum(self, num: int) -> None:
        """Add a number into the data structure."""
        if len(self.lower) == 0:
            self.lower.append(-num)
            return
        if len(self.upper) == 0:
            self.upper.append(num)
            return
        
        if len(self.lower) == len(self.upper):
            if num >= self.upper[0]:
                top = heapq.heappop(self.upper)
                heapq.heappush(self.lower, -top)
                heapq.heappush(self.upper, num)
            else: heapq.heappush(self.lower, -num)
        else:
            if num <= -self.lower[0]:
                top = -heapq.heappop(self.lower)
                heapq.heappush(self.upper, top)
                heapq.heappush(self.lower, -num)
            else: heapq.heappush(self.upper, num)
        
    def findMedian(self) -> float:
        """Return the current median."""
        if len(self.lower) == len(self.upper): return (-self.lower[0] + self.upper[0]) / 2
        else: return -self.lower[0]


# ---------------------------
# Level 3
# ---------------------------

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    LeetCode #253: Meeting Rooms II
    Given intervals [start, end), return the minimum number of rooms required.

    Approach:
      - Sort by start time
      - Use a min-heap of end times; when a meeting ends (heap top <= next start), pop.

    Example:
      [[0,30],[5,10],[15,20]] -> 2
    """
    raise NotImplementedError


def reorganize_string(s: str) -> str:
    """
    LeetCode #767: Reorganize String
    Rearrange s so that no two adjacent characters are the same.
    If impossible, return "".

    Typical approach:
      - Max-heap by counts; greedily pick the top two different chars each step.

    Examples:
      "aab" -> "aba"
      "aaab" -> ""
    """
    raise NotImplementedError


# ---------------------------
# Helper utilities for tests
# ---------------------------

def build_list(values: Iterable[int]) -> Optional[ListNode]:
    head = curr = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = curr = node
        else:
            assert curr is not None
            curr.next = node
            curr = node
    return head

def list_to_pylist(head: Optional[ListNode]) -> List[int]:
    out: List[int] = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# ---------------------------
# Tests (initially marked as expected failures)
# Remove @expectedFailure on a test when your solution is ready.
# ---------------------------

class TestLevel1(unittest.TestCase):
    def test_kth_largest_basic(self):
        self.assertEqual(kth_largest([3,2,1,5,6,4], 2), 5)
        self.assertEqual(kth_largest([3,2,3,1,2,4,5,5,6], 4), 4)

    def test_last_stone_weight_basic(self):
        self.assertEqual(last_stone_weight([2,7,4,1,8,1]), 1)
        self.assertEqual(last_stone_weight([1]), 1)
        self.assertEqual(last_stone_weight([9,3]), 6)


class TestLevel2(unittest.TestCase):
    def test_merge_k_lists_basic(self):
        l1 = build_list([1,4,5])
        l2 = build_list([1,3,4])
        l3 = build_list([2,6])
        out = merge_k_lists([l1, l2, l3])
        self.assertEqual(list_to_pylist(out), [1,1,2,3,4,4,5,6])

    def test_top_k_frequent_basic(self):
        self.assertCountEqual(top_k_frequent([1,1,1,2,2,3], 2), [1,2])
        self.assertCountEqual(top_k_frequent([1], 1), [1])
        # multiple answers valid
        self.assertCountEqual(top_k_frequent([4,4,4,6,6,7,7,7,7], 2), [7,4])

    def test_median_finder_basic(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2.0)

        mf2 = MedianFinder()
        for x in [5, 15, 1, 3]:
            mf2.addNum(x)
        self.assertEqual(mf2.findMedian(), 4.0)


class TestLevel3(unittest.TestCase):
    def test_min_meeting_rooms_basic(self):
        self.assertEqual(min_meeting_rooms([[0,30],[5,10],[15,20]]), 2)
        self.assertEqual(min_meeting_rooms([[7,10],[2,4]]), 1)
        self.assertEqual(min_meeting_rooms([[1,5],[2,6],[4,8]]), 3)

    def test_reorganize_string_basic(self):
        self.assertIn(reorganize_string("aab"), {"aba"})
        self.assertEqual(reorganize_string("aaab"), "")

if __name__ == "__main__":
    unittest.main()
