package main

import (
	"fmt"
	"strconv"
	"strings"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	fmt.Println("Hello world")
	l1 := createListNode([]int{-6, -5, 6, 6, 7})
	l2 := createListNode([]int{0})
	l3 := mergeTwoLists(&l1, &l2)
	fmt.Println(stringList(l3))
}

func stringList(node *ListNode) string {
	var listString strings.Builder
	for node != nil {
		val := strconv.Itoa(node.Val)
		listString.WriteString(val)
		if node.Next != nil {
			listString.WriteString(" -> ")
		}
		node = node.Next
	}
	return listString.String()
}

func createListNode(list []int) ListNode {
	node := &ListNode{list[0], nil}
	head := node
	for _, num := range list[1:] {
		node.Next = &ListNode{num, nil}
		node = node.Next
	}
	return *head
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := &ListNode{}
	current := dummy
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			current.Next = list1
			list1 = list1.Next
		} else {
			current.Next = list2
			list2 = list2.Next
		}
		current = current.Next
	}

	if list1 != nil {
		current.Next = list1
	} else if list2 != nil {
		current.Next = list2
	}

	return dummy.Next
}
