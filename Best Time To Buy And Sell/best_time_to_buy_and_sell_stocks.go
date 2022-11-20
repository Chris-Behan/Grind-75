package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
}

func maxProfit(prices []int) int {
	minPrice := math.MaxInt
	maxProfit := 0
	for _, p := range prices {
		if p < minPrice {
			minPrice = p
		}
		diff := p - minPrice
		if diff > maxProfit {
			maxProfit = diff
		}
	}
	return maxProfit
}
