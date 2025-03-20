from typing import List
import heapq

# compute each point's distance dict
# use heap to store distance as keys
# pop k distances and find their points in dict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance_dict = {}
        for point in points:
            dist = ((point[0])**2 + (point[1])**2)
            if dist not in distance_dict:
                distance_dict[dist] = [point]
            else:
                distance_dict[dist].append(point)
        
        heap = list(distance_dict.keys())
        heapq.heapify(heap)
        
        answer = []
        while k > 0:
            dist = heapq.heappop(heap)
            answer += distance_dict[dist]
            k -= len(distance_dict[dist])
        
        return answer
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1,3],[-2,2]], 1))
    print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))
    print(sol.kClosest([[0,1],[1,0]], 2))
