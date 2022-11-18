# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list_node(l: list) -> ListNode | None:
    if not l:
        return None
    head = pointer = ListNode(l[0])
    for n in l[1:]:
        pointer.next = ListNode(n)
        pointer = pointer.next
    return head


def list_str(node: ListNode | None) -> str:
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    str_list = " -> ".join(vals)
    return str_list


def mergeTwoLists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    # handle empty lists
    if not l1:
        return l2
    if not l2:
        return l1
    # Set current pointer and reference to head which will be returned
    if l1.val <= l2.val:
        head = current = l1
        l1 = l1.next
    else:
        head = current = l2
        l2 = l2.next

    while l1 or l2:
        if l1 and l2 and l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        elif l1 and l2 and l2.val <= l1.val:
            current.next = l2
            l2 = l2.next
        elif not l1:
            current.next = l2
            l2 = l2.next
        elif not l2:
            current.next = l1
            l1 = l1.next
        current = current.next

    return head


def mergeTwoLists2(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    Approach: Create a "current" pointer representing the current head of the list, then traverse
    both lists, setting the current pointer's 'next' value to whichever node has a smaller 'val'.
    After setting the current pointer's 'next' value to one of the nodes, l1 or l2, we
    increment the selected node by setting itself to it's next value: ex l1 = l1.next. This is
    how the traversal is done.
    Once either of the input lists has reached the end and is thus None, we set current.next to
    the non-None remaining list, if any. This will handle the scenario where one list is longer
    than the other.

    Time Complexity: O(n + m)
    We do a linear traversal through each input list. Thus if the input lists are size n and m,
    the run time is O(n + m).

    Space Complexity O(n + m):
    Input size is n + m where n is the length of l1 and m is the length of l2. Our algorithm itself
    creates a constant amount of extra space with the dummy node, which is less than the n and m
    size of the input.

    Auxiliary space: O(1)
    Regardless the size of the input, our algorithm only creates a single dummy ListNode to maintain
    a reference to the head of the list.


    Args:
        l1 (ListNode | None): sorted list
        l2 (ListNode | None): sorted list

    Returns:
        ListNode | None: sorted merged list
    """
    dummy = current = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next


l1 = create_list_node([1, 2, 4])
l2 = create_list_node([1, 3, 4])
l5 = mergeTwoLists2(l1, l2)
