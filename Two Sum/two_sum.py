def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Approach: First, create a map of whose keys are numbers in the list and whose values are the
    indices at which the number appears in the list.
    Then iterate through the original list of numbers, calculating what other number would be
    needed to reach the target, and checking if that other number exists in the map. If the 
    number does exist in the map, make sure its index is different from the number of the current
    iteration. Since there is only 1 possible answer per input, return the answer once it is found.

    Time Complexity: O(n) 
    Explanation: We are performing 2 iterations of length n. One to build the map, and one to do
    the comparison. n + n is still asymptotically bounded by O(n).

    Space Complexity: O(n)
    Since the input is O(n), the minimum space complexity for the answer is O(n).
    We create an additional data-structure (the map) of size 2n, but n + 2n is still asymptotically
    bounded by O(n).

    Auxiliary space: O(n)
    We use O(n) extra space to create the map.

    Args:
        nums (list[int]): input list of numbers
        target (int): desired target sum

    Returns:
        list[int]: indices of the two values in nums that add up to target.
    """
    nums_idx_map = {}
    for idx, num in enumerate(nums):
        nums_idx_map[num] = idx

    for idx, num in enumerate(nums):
        other = target - num
        if other in nums_idx_map and nums_idx_map[other] != idx:
            return [idx, nums_idx_map[other]]


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
