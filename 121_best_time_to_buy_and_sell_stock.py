#2025-10-17 time: 9:20
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = max(profit,prices[right]-prices[left])
            else:
                left = right
            right+=1
        return profit