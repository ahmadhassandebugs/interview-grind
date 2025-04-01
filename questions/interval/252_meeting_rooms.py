from typing import List

# [s1, e1] [s2, e2]
# s1 <-----------> e1
#           s2<------>e2
# s1 <= e2 and s2 <= e1

# a person can attend all meetings if no overlap
#   two for loops and comparison O(n)
# we can sort the array on first start time
#   and then compare in a single loop

# pay attention to equal sign in condition

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][0] < intervals[i+1][1] and intervals[i+1][0] < intervals[i][1]:
                return False
        return True
            
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canAttendMeetings([[0,30],[5,10],[15,20]]))
    print(sol.canAttendMeetings([[7,10],[2,4]]))
    print(sol.canAttendMeetings([[13,15],[1,13]]))
