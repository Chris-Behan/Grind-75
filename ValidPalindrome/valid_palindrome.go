package main

import (
	"fmt"
	"regexp"
	"strings"
)

func main() {
	fmt.Print(isPalindrome("Rac!!!!ecar'"))
}

func isPalindrome(s string) bool {
	lowercase := strings.ToLower(s)
	fmt.Printf("lowercase: %v\n", lowercase)
	lowercaseAlphanumeric := removeNonAlphaumeric(lowercase)
	fmt.Printf("lowercase alphanumeric: %v\n", lowercaseAlphanumeric)
	reversed := reversedRunes(lowercaseAlphanumeric)
	fmt.Printf("reversed lowercase alphanumeric: %v\n", reversed)
	for idx, r := range lowercaseAlphanumeric {
		if r != reversed[idx] {
			return false
		}
	}
	return true
}

func removeNonAlphaumeric(s string) string {
	var alphanumeric strings.Builder
	alphanumericRegex, _ := regexp.Compile("[A-Za-z0-9]")
	for _, r := range s {
		if alphanumericRegex.MatchString(string(r)) {
			alphanumeric.WriteRune(r)
		}
	}
	return alphanumeric.String()
}

func reversedRunes(s string) []rune {
	reversed := []rune{}
	for i := len(s) - 1; i >= 0; i-- {
		reversed = append(reversed, rune(s[i]))
	}
	return reversed
}
