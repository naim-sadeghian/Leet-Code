class Solution:
    """
    Update minimum at each step and compare the price of selling based on minimum

    Time Complexity: O(n) iterate through whole list
    Space Complexity: O(1) 
    """
    def maxProfit(self, prices: List[int]) -> int:
        net = 0
        buy = float('inf')
        for price in prices:
            buy = min(buy, price)
            net = max(net, price-buy)
        return net