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

    Examples:
      [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
      [[1,4],[4,5]] -> [[1,5]]   (closed intervals sharing a bound should merge)
    """
    pass


# ----------------------------------------------------
# 2) Insert Interval (LC 57)
# ----------------------------------------------------
def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Given a set of non-overlapping intervals sorted by start time, insert a new interval
    into the intervals (merge if necessary).
    
    Examples:
      intervals = [[1,3],[6,9]], new = [2,5]      -> [[1,5],[6,9]]
      intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new = [4,8]
        -> [[1,2],[3,10],[12,16]]
    """
    pass


# ----------------------------------------------------
# 3) Meeting Rooms I (LC 252)
# ----------------------------------------------------
def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Return True if a single person can attend all meetings (no overlaps).

    Examples (treating as half-open):
      [[0,30],[5,10],[15,20]] -> False
      [[7,10],[2,4]] -> True
      [[1,2],[2,3]] -> True  (touching is OK)
    """
    pass

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
