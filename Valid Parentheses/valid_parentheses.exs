defmodule ValidParentheses do
  @doc """
  Approach: Recursive solution that builds up a stack of open brackets (final is_valid function).
  Whenever a closed bracket is encountered, ensure the top of the stack is the corresponding open
  bracket. If not, return false. If we reach the end of the string and have an empty stack, the
  parentheses are valid. If we reach the end of the string but the stack is not empty, the
  parentheses are invalid.
  
  Time Complexity: O(n)
  We convert the string into a list of codepoints (likely an n step operation) then we iterate
  through that list of codepoints.
  
  Space Complexity: O(n)
  Input is a string of size n. We perform n function calls, so the call stack is also of size n,
  but n + n is still O(n).
  
  Auxiliary space: O(n)
  We create a stack of the open parentheses, which is potentially n items long in the worst case.
  """
  def is_valid(string) when is_binary(string) do
    is_valid(String.codepoints(string))
  end

  def is_valid([], []), do: true
  def is_valid([], tail), do: false

  def is_valid([head | tail], stack \\ []) do
    cond do
      head == "(" or head == "[" or head == "{" -> is_valid(tail, [head | stack])
      length(stack) == 0 -> false
      head == ")" and hd(stack) == "(" -> is_valid(tail, tl(stack))
      head == "]" and hd(stack) == "[" -> is_valid(tail, tl(stack))
      head == "}" and hd(stack) == "{" -> is_valid(tail, tl(stack))
      true -> false
    end
  end
end
