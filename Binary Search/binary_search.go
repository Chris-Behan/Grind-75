package main

import "fmt"

func main() {
	res1 := search([]int{-3, -1, 0, 1, 4, 44, 313}, -1)
	res2 := search([]int{-3, -1, 0, 1, 4, 44, 313}, -3)
	res3 := search([]int{-3, -1, 0, 1, 4, 44, 313}, 313)
	res4 := search([]int{-3, -1, 0, 1, 4, 44, 313}, -4)
	fmt.Println(res1)
	fmt.Println(res2)
	fmt.Println(res3)
	fmt.Println(res4)
}

func search(nums []int, target int) int {
	low := 0
	high := len(nums) - 1
	for low <= high {
		mid := (low + high) / 2
		midNum := nums[mid]
		if midNum == target {
			return mid
		} else if midNum < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}
