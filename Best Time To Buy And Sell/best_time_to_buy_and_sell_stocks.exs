defmodule Solution do
  @spec max_profit(prices :: [integer]) :: integer
  def max_profit(prices) do
    Solution.max_profit(prices, 999_999, 0)
  end

  def max_profit([], _, profit) do
    profit
  end

  def max_profit([today | prices], min_price, profit) do
    min_price = if today < min_price, do: today, else: min_price
    diff = today - min_price
    profit = if diff > profit, do: diff, else: profit
    Solution.max_profit(prices, min_price, profit)
  end
end

profit = Solution.max_profit([7, 1, 5, 3, 6, 4])
IO.inspect(profit)
