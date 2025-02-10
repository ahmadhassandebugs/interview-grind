# nums = [1,1,1,2,2,3], k = 2
# create a freq count dict
# find top k based on the count
# return respective keys

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict  = {}
        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        heap = []
        for num, freq in freq_dict.items():
            heapq.heappush(heap, (-freq, num))
        res = []
        while len(res) < k:  # O(klogn)
            res.append(heapq.heappop(heap)[1])
        return res
    
    def topKFrequent_v1(self, nums: List[int], k: int) -> List[int]:
        freq_dict  = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        freq_dict = list(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))  # O(nlogn)
        return [item[0] for item in freq_dict[:k]]
    
if __name__=="__main__":
    tc1 = [1,1,1,2,2,3], 2
    tc2 = [1], 1
    sol = Solution()
    print(sol.topKFrequent(*tc1))
    print(sol.topKFrequent(*tc2))
