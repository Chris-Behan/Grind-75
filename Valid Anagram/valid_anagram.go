package main

import "fmt"

func main() {
	res := isAnagram("hello", "olelhh")
	fmt.Println(res)
}

func isAnagram(s string, t string) bool {
	sCounts := runeCounts(s)
	tCounts := runeCounts(t)
	if len(sCounts) != len(tCounts) {
		return false
	}
	for key1, val1 := range sCounts {
		if val2, found := tCounts[key1]; !found || val2 != val1 {
			return false
		}
	}

	return true
}

func runeCounts(s string) map[rune]int {
	counts := map[rune]int{}
	for _, r := range s {
		if _, found := counts[r]; found {
			counts[r]++
		} else {
			counts[r] = 1
		}
	}
	return counts
}
