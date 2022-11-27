from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Approach: Base case is that the node/root is None and we return None.
    Start by calling the function recursively on the left and right nodes, then swap
    the left child and right child. This is a top-down recursive approach, in which the recursive
    calls will go depth-first to the bottom of the tree, swapping out the left and right nodes.
    The calls will then unfold, swapping the left and right nodes of the parent. Since the prior
    calls already swapped the children nodes and the parent nodes have a reference to those
    swapped children, it has the effect of inverting the entire tree.

    Time Complexity: O(n)
    We recursively iterate through each node in the tree.

    Space Complexity: O(n)
    call-stack will be n in the worst case.

    Auxiliary space: O(n)
    Call stack will be n in the worst case.

    Args:
        root (Optional[TreeNode]): _description_

    Returns:
        Optional[TreeNode]: _description_
    """
    if root:
        invertTree(root.left)
        invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
    return root


def list_to_treenode(nums: list[int], idx: int) -> Optional[TreeNode]:
    node = None
    if idx < len(nums):
        node = TreeNode(nums[idx])
        node.left = list_to_treenode(nums, 2 * idx)
        node.right = list_to_treenode(nums, 2 * idx + 1)
    return node


def print_treenode(root: Optional[TreeNode]):
    if root:
        print(root.val)
        print_treenode(root.left)
        print_treenode(root.right)


print("Before")
root2 = list_to_treenode([0, 4, 2, 7, 1, 3, 6, 9], 1)
print_treenode(root2)
print("After")
inverted = invertTree(root2)
print_treenode(root2)
