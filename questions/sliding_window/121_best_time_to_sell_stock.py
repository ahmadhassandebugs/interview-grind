# [7,1,5,3,6,4]
# it's a sliding window problem
#   first element in the window is buy point: l
#   last element in the window is sell point: r
#   profit = sell - buy
#   window is variable sized
#   find the window that maximizes the profit
# keep moing window right and update max_profit
# we update left if it's the minimum we have encountered so far


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, l, r = 0, 0, 1

        while r < len(prices):
            if prices[r] < prices[l]: l = r
            elif prices[r] - prices[l] > max_profit: max_profit = prices[r] - prices[l]
            r += 1
        
        return max_profit
        

if __name__ == "__main__":
    tc1 = [7,1,5,3,6,4]
    tc2 = [7,6,4,3,1]
    sol = Solution()
    print(sol.maxProfit(tc1))
    print(sol.maxProfit(tc2))
