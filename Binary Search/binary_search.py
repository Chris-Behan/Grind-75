def search(nums: list[int], target: int) -> int:
    """
    Approach: Iterative binary search. Initialize low and high pointers, then iterate through the
    list, checking if the value between the two pointers (mid) is equal to the target. If the
    mid value is less than the target, we know that our target must be to the right (since it's
    a sorted ascending order list) so we set the low pointer to mid + 1. If the mid value is greater
    than the target, we know our target will be to the left, so we set high to mid -1. If there
    reaches a time when low > high, stop iterating and return -1.

    Args:
        nums (list[int]): sorted ascending order list
        target (int): number we are looking for

    Returns:
        int: index at which the number occurs or -1
    """
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        mid_num = nums[mid]
        if mid_num == target:
            return mid
        elif mid_num > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


res1 = search([-2, -1, 0, 2, 3, 4, 11, 99, 101], -2)
print(res1)
