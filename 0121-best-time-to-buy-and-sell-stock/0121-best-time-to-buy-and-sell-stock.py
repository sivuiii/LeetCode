class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # buy = 0
        # for i in range(len(prices)-1) :
        #     for j in range(i+1, len(prices)) :
        #         if i >= j :
        #             continue
        #         buy = max(buy, prices[j]-prices[i])
        # return buy
        bp, op = 10001 , 0
        for price in prices :
            if price < bp :
                bp = price
            else :
                op =max(op, price-bp)

        return op

