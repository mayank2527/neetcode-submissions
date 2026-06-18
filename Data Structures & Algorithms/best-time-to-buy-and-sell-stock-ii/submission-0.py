class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total_profit = 0
        current_profit = 0
        buy_price = prices[0]

        for price in prices[1:]:
            if price - buy_price > current_profit:
                current_profit = price - buy_price
            else:
                buy_price = price
                if current_profit > 0:
                    total_profit += current_profit
                    current_profit = 0
        
        if current_profit > 0:
            total_profit+=current_profit

        return total_profit