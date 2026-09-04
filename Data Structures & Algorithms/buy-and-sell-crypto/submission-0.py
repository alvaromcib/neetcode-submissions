class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        maximum_profit = 0

        n = len(prices)

        for i in range(n):

            r = l

            while r <= n - 1:
                maximum_profit = max(maximum_profit, prices[r] - prices[l])
                r += 1
            l += 1

        return maximum_profit
        