package main

import "fmt"

func main() {
	img := [][]int{
		{1, 1, 1},
		{0, 0, 0},
	}
	floodFill(img, 1, 1, 0)
	drawImage(img)
}

// Approach: First check if the new color is different from the source, if not
// return the image immediately. Otherwise, perform a depth first search
// 4-directionally on the source pixel. My dfs function does bounds checking before
// it makes each recursive call. Since I know the initial pixel is valid, I can simplify
// the logic in my bounds checking, only calling the left, right, up, and down pixels
// when the current pixel coordinate is a certain value. For example, only search the pixel to my
// left if the current pixel's column value is greater than 0.
//
// Time Complexity: O(r * c)
// In the worse case the dfs will traverse every pixel in image.
//
// Space Complexity: O(r * c)
// Image is of size r * c. Depth first search in the worse case will add an additional r * c
// stack frames.
//
// Auxiliary memory: O(r * c)
// Depth first search in the worst case will add (r * c) stack frames.
func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	if color == image[sr][sc] {
		return image
	}
	dfsFill(image, image[sr][sc], color, sr, sc)
	return image
}

func dfsFill(image [][]int, oldColor int, newColor int, sr int, sc int) {
	if image[sr][sc] == oldColor {
		image[sr][sc] = newColor
		if sr > 0 {
			dfsFill(image, oldColor, newColor, sr-1, sc)
		}
		if sr < len(image)-1 {
			dfsFill(image, oldColor, newColor, sr+1, sc)
		}
		if sc > 0 {
			dfsFill(image, oldColor, newColor, sr, sc-1)
		}
		if sc < len(image[0])-1 {
			dfsFill(image, oldColor, newColor, sr, sc+1)
		}
	}
}

func drawImage(image [][]int) {
	for _, row := range image {
		fmt.Println(row)
	}
}
