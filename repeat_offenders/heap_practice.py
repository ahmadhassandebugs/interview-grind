from __future__ import annotations
from typing import List, Optional, Iterable
import heapq
import unittest
from dataclasses import dataclass

def kth_largest(nums: List[int], k: int) -> int:
    """
    LeetCode #215: Kth Largest Element in an Array
    Return the kth largest element in the unsorted array.

    Examples:
      nums = [3,2,1,5,6,4], k=2 -> 5
      nums = [3,2,3,1,2,4,5,5,6], k=4 -> 4
    """
    pass


def last_stone_weight(stones: List[int]) -> int:
    """
    LeetCode #1046: Last Stone Weight
    Repeatedly smash the two heaviest stones; if unequal, push back the difference.

    Examples:
      stones = [2,7,4,1,8,1] -> 1
    """
    pass


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
    pass


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    LeetCode #347: Top K Frequent Elements
    Return any ordering of the k most frequent elements.

    Example:
      nums = [1,1,1,2,2,3], k=2 -> [1,2]
    """
    pass


class MedianFinder:
    """
    LeetCode #295: Find Median from Data Stream
    """
    def __init__(self) -> None:
        pass
    
    def addNum(self, num: int) -> None:
        pass
        
    def findMedian(self) -> float:
        pass

# ---------------------------
# Level 3
# ---------------------------

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    LeetCode #253: Meeting Rooms II
    Given intervals [start, end), return the minimum number of rooms required.

    Example:
      [[0,30],[5,10],[15,20]] -> 2
    """
    pass

def reorganize_string(s: str) -> str:
    """
    LeetCode #767: Reorganize String
    Rearrange s so that no two adjacent characters are the same.
    If impossible, return "".

    Examples:
      "aab" -> "aba"
      "aaab" -> ""
    """
    pass


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
