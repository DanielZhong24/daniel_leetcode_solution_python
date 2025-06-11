#2025-6-11 time: 9:20
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_price =0 
        min_price = float('inf')

        for p in prices:
            max_price = max(max_price,p-min_price)

            min_price = min(p,min_price)
        return max_price