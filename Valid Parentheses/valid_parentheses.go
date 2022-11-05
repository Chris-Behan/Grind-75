package main

import "fmt"

func main() {
	fmt.Println(isValid("()[]{}"))
}

func isValid(s string) bool {
	parenthesis := map[rune]rune{'(': ')', '[': ']', '{': '}'}
	stack := []rune{}
	for _, p := range s {
		_, openP := parenthesis[p]
		if openP {
			stack = append(stack, p)
		} else {
			if len(stack) == 0 {
				return false
			}
			var topOfStack rune
			topOfStack, stack = stack[len(stack)-1], stack[:len(stack)-1]
			if parenthesis[topOfStack] != p {
				return false
			}
		}
	}
	return len(stack) == 0
}
