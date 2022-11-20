defmodule ListNode do
  @type t :: %__MODULE__{
          val: integer,
          next: ListNode.t() | nil
        }
  defstruct val: 0, next: nil
end

defmodule Solution do
  @spec merge_two_lists(list1 :: ListNode.t() | nil, list2 :: ListNode.t() | nil) ::
          ListNode.t() | nil
  def merge_two_lists(list1, list2) do
    head = %ListNode{}
    merge_two_lists(head, list1, list2)
    head.next
  end

  def merge_two_lists(head, nil, nil), do: nil
  def merge_two_lists(head, list1, nil), do: head = %{head | next: list1}
  def merge_two_lists(head, nil, list2), do: head = %{head | next: list2}

  def merge_two_lists(head, list1, list2) do
    if list1.val <= list2.val do
      head = %{head | val: list1.val}
      head = %{head | next: merge_two_lists(%ListNode{}, )}
    else
      2
    end
  end

  def create_list_node([head | []]) do
    %ListNode{val: head}
  end

  def create_list_node([head | tail]) do
    node = %ListNode{val: head, next: Solution.create_list_node(tail)}
  end
end

l1 = Solution.create_list_node([1, 2, 3])
IO.inspect(l1)
l2 = Solution.create_list_node([1, 3, 4])
IO.inspect(l2)

Solution.merge_two_lists(l1, l2)
