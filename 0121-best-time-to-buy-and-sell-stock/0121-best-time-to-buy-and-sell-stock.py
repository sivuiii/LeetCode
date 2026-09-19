class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bp, op = 10001 , 0
        for price in prices :
            if price < bp :
                bp = price
            else :
                op =max(op, price-bp)

        return op

