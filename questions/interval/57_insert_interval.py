from typing import List

# find all overlapping intervals
# join overlapping intervals with the new one
# place the new interval inside the original array

# pay attention to inserting and whether to start from left or right depending on less than
#   or greater than comparison

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def find_overlaps():
            nonlocal intervals, newInterval
            overlaps, remaining = [], []
            for interval in intervals:
                if interval[0] <= newInterval[1] and newInterval[0] <= interval[1]:
                    overlaps.append(interval)
                else:
                    remaining.append(interval)
            return overlaps, remaining
        
        def merge_overlaps(intervals):
            if not intervals: return newInterval
            min_start = min(intervals[0][0], newInterval[0])
            max_end = max(intervals[-1][1], newInterval[1])
            return [min_start, max_end]
        
        def insert_interval(remaining, new_merged_interval):
            if not remaining: return [new_merged_interval]
            
            if new_merged_interval[1] < remaining[0][0]:
                remaining.insert(0, new_merged_interval)
                return remaining
            
            for i in range(len(remaining)-1, -1, -1):
                if new_merged_interval[0] > remaining[i][1]:
                    remaining.insert(i+1, new_merged_interval)
                    return remaining
        
        if not intervals: return [newInterval]            
        overlaps, remaining = find_overlaps()
        new_merged_interval = merge_overlaps(overlaps)
        answer = insert_interval(remaining, new_merged_interval)
        return answer

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1,3],[6,9]], [2,5]))
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(sol.insert([[2,6],[7,9]], [15,18]))
    print(sol.insert([[1,5]], [2,3]))
