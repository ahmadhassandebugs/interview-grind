from typing import List

# sort the intervals so that we can compare neighbors
# iterate over the array
#   if overlap found, merge the overlap and add merged interval to the array
#   else add the interval to the array

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort( key=lambda x: x[0] )
        
        answer = []
        for i in range(len(intervals) - 1):
            if intervals[i][0] <= intervals[i+1][1] and intervals[i+1][0] <= intervals[i][1]:
                start = min(intervals[i][0], intervals[i+1][0])
                end = max(intervals[i][1], intervals[i+1][1])
                new_interval = [start, end]
                intervals[i+1] = new_interval
            else:
                answer.append(intervals[i])
        
        answer.append(intervals[-1])
        return answer
                
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(sol.merge([[1,4],[4,5],[5,8]]))
    print(sol.merge([[1,4],[6,8]]))
    