defmodule TwoSum do
  @doc """
  Approach: Create a map of numbers to indices at which the numbers appear using a generator and :into.
  Then use a reduce on the original list of numbers and their indices.
  The reduce first calculates the compliment needed to sum to the target.
  It then checks if the compliment is in the map, and if it is, checks that its value is different
  than the index of the current iteration. If this is the case, a 2 element list of the two
  indices is returned. Otherwise, the accumulator value is returned. It is important to note we
  initialize the accumulator to an empty list so that the reduce starts on the first element of the
  input list.
  
  Time Complexity: O(n)
  We iterate through a list of n elements 3 times, once to create the list of tuples, once to create
  the map, and once to perform the reduce.
  
  Space Complexity: O(n)
  Input is O(n), we use that input to create 2 collections of size 2n, but n + 2n + 2n is still O(n)
  
  Auxiliary space: O(n)
  We create a list of tuples of size 2n (2n because each tuple is 2 elements) and a map of size 2n
  (2n because there is a key and value for each n).
  """
  def two_sum(nums, target) do
    num_idx_tuples = Enum.with_index(nums)

    nums_idx_map =
      for {num, idx} <- num_idx_tuples, into: %{} do
        {num, idx}
      end

    num_idx_tuples
    |> Enum.reduce([], fn {num, idx}, acc ->
      compliment = target - num

      if nums_idx_map[compliment] && nums_idx_map[compliment] != idx do
        [idx, nums_idx_map[compliment]]
      else
        acc
      end
    end)
  end
end

IO.inspect(TwoSum.two_sum([2, 7, 11, 15], 9))
IO.inspect(TwoSum.two_sum([3, 2, 4], 6))
IO.inspect(TwoSum.two_sum([3, 3], 6))
