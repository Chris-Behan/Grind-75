
def maxProfit(prices: list[int]) -> int:
    """
    Approach: First we initialize the min price to infinity and the max profit to 0.
    We then iterate through the list of prices, setting the min price to the current
    price if the current price is less than the min, which it is guaranteed to be on
    the first iteration since we initialized the min price to infinity. Then we check
    if the current price minus the min price is greater than the max profit. If so, 
    we set the max profit to this value. Since we initialize max profit to 0, 
    it will only be overriden if the current price minus the min value is > 0.
    This works because we set the min price first and if there is ever a current price
    that is greater than the min, the max profit will be set to the difference of the
    2 values. If the min price is always the same as the current price, the max profit
    will be 0, and if the min price is greater than the current price, the difference
    will be negative and the max profit will never be set.

    Time Complexity: O(n)
    We iterate through the list of prices once.

    Space Complexity: O(n)
    We receive a list of n prices.

    Auxiliary space: O(1)
    Regardless of the input size, we only ever have 3 extra variables in memory, the min_price,
    max_profit, and p.

    Args:
        prices (list[int]): list of prices for each day

    Returns:
        int: max profit that can be made
    """
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        if p < min_price:
            min_price = p
        if p - min_price > max_profit:
            max_profit = p - min_price
    return max_profit


prices = [7, 1, 5, 3, 6, 5]
profit = maxProfit(prices)
print(profit)
prices2 = [7, 6, 4, 3, 1]
print(maxProfit(prices2))
