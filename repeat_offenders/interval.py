# intervals_practice.py
# ----------------------------------------------------
# Interval practice scaffold (NO SOLUTIONS)
# 1) Merge Intervals           (LC 56)
# 2) Insert Interval           (LC 57)
# 3) Meeting Rooms I (feasibility) (LC 252)
#
# How to use:
# - Implement the functions (replace NotImplementedError)
# - Run: python -m unittest intervals_practice.py
# - Remove @expectedFailure from a test when you finish its function.
# ----------------------------------------------------

from __future__ import annotations
from typing import List
import unittest


# ----------------------------------------------------
# 1) Merge Intervals (LC 56)
# ----------------------------------------------------
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge all overlapping intervals and return a new list of non-overlapping intervals
    that cover all the intervals in the input.

    Notes:
      - Intervals are [start, end]; assume start <= end.
      - Typical approach: sort by start, then merge in one pass.
      - For half-open intervals [start, end) adjust overlap rule accordingly.

    Examples:
      [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
      [[1,4],[4,5]] -> [[1,5]]   (closed intervals sharing a bound should merge)
    """
    # Brute-force: If i and i+1 overlap (end of i >= start of i+1), merge them
    #              O(n) time; O(n) space
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])  # sort on start times
    res = []
    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res


# ----------------------------------------------------
# 2) Insert Interval (LC 57)
# ----------------------------------------------------
def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Given a set of non-overlapping intervals sorted by start time, insert a new interval
    into the intervals (merge if necessary).

    Hints:
      - Append all intervals that end before new_interval starts.
      - Merge all intervals that overlap new_interval into a single expanded interval.
      - Append the rest.

    Examples:
      intervals = [[1,3],[6,9]], new = [2,5]      -> [[1,5],[6,9]]
      intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new = [4,8]
        -> [[1,2],[3,10],[12,16]]
    """
    res = []
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    res.append(new_interval)
    while i < n:
        res.append(intervals[i])
        i += 1
    return res


# ----------------------------------------------------
# 3) Meeting Rooms I (LC 252)
# ----------------------------------------------------
def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Return True if a single person can attend all meetings (no overlaps).

    Assumptions:
      - Treat as closed intervals [s, e] or half-open [s, e); choose and be consistent.
      - For half-open [s, e), 'touching' meetings where next.start == prev.end do NOT overlap.

    Examples (treating as half-open):
      [[0,30],[5,10],[15,20]] -> False
      [[7,10],[2,4]] -> True
      [[1,2],[2,3]] -> True  (touching is OK)
    """
    # Can attend if no overlap: (s1, e1) (s2, e2) when s1 <= s2. Overlap can happen
    # if e1 > s2.
    intervals.sort(key= lambda x: x[0])
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]: return False
    return True


# ----------------------------------------------------
# Tests (initially marked as expected failures)
# Remove @expectedFailure when you finish an implementation.
# ----------------------------------------------------

class TestMergeIntervals(unittest.TestCase):
    def test_merge_basic(self):
        self.assertEqual(
            merge_intervals([[1,3],[2,6],[8,10],[15,18]]),
            [[1,6],[8,10],[15,18]],
        )
        self.assertEqual(
            merge_intervals([[1,4],[4,5]]),
            [[1,5]],
        )

    def test_merge_edge_cases(self):
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([[1,4]]), [[1,4]])
        # already non-overlapping
        self.assertEqual(merge_intervals([[1,2],[3,4],[5,6]]), [[1,2],[3,4],[5,6]])
        # nested intervals
        self.assertEqual(merge_intervals([[1,10],[2,3],[4,8]]), [[1,10]])


class TestInsertInterval(unittest.TestCase):
    def test_insert_basic(self):
        self.assertEqual(
            insert_interval([[1,3],[6,9]], [2,5]),
            [[1,5],[6,9]],
        )
        self.assertEqual(
            insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
            [[1,2],[3,10],[12,16]],
        )

    def test_insert_edge_cases(self):
        self.assertEqual(insert_interval([], [2,5]), [[2,5]])
        self.assertEqual(insert_interval([[1,5]], [2,3]), [[1,5]])
        self.assertEqual(insert_interval([[1,2],[3,4]], [5,6]), [[1,2],[3,4],[5,6]])
        # insert before all
        self.assertEqual(insert_interval([[5,7],[8,12]], [1,3]), [[1,3],[5,7],[8,12]])
        # insert after all
        self.assertEqual(insert_interval([[1,3],[4,6]], [7,9]), [[1,3],[4,6],[7,9]])


class TestCanAttendMeetings(unittest.TestCase):
    def test_meeting_rooms_basic(self):
        self.assertFalse(can_attend_meetings([[0,30],[5,10],[15,20]]))
        self.assertTrue(can_attend_meetings([[7,10],[2,4]]))

    def test_meeting_rooms_touching(self):
        # Treat intervals as half-open [s, e): touching is allowed
        self.assertTrue(can_attend_meetings([[1,2],[2,3],[3,4]]))
        # Overlap present
        self.assertFalse(can_attend_meetings([[1,3],[2,4]]))

    def test_meeting_rooms_edges(self):
        self.assertTrue(can_attend_meetings([]))
        self.assertTrue(can_attend_meetings([[1,1]]))   # zero-length meeting allowed -> no conflict


if __name__ == "__main__":
    unittest.main()
