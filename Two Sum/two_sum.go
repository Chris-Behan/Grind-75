package main

import "fmt"

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSum([]int{3, 2, 4}, 6))
}

// Approach: Create a map whose keys are numbers in the list and whose values are the indices at
// at which the numbers appear.
// Then iterate through the original list of numbers, calculating the other number required to
// sum to the target. If the other number exists in the map, ensure its index is different from
// the index of the number we are currently iterating on, as we the indices must be unique.
// Once we have found the two numbers that sum to the target, return them in a 2 element list.
//
// Time complexity: O(n)
// We perform two iterations on slice of size n, and n + n = 2n = O(n)
//
// Space Complexity: O(n)
// The input to the algorithm is a slice of size n. We also create a map of size 2n.
// n + 2n = 3n = O(n)
//
// Auxiliary space: O(n)
// We create a map of size 2n (2 elements, a key and a value, per element in the input list).
func twoSum(nums []int, target int) []int {
	numsIdxMap := make(map[int]int)
	for idx, val := range nums {
		numsIdxMap[val] = idx
	}

	for idx, n := range nums {
		other := target - n
		if idxInMap, nInMap := numsIdxMap[other]; nInMap && idxInMap != idx {
			return []int{idx, idxInMap}
		}
	}
	return []int{}
}
