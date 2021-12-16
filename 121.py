class Solution:
     def maxProfit(self, prices: List[int]) -> int:
            min_price = float('inf')
            max_operation = 0
            for price in prices:
                min_price = min(min_price, price)
                operation = price - min_price
                max_operation = max(max_operation, operation)
            return max_operation
