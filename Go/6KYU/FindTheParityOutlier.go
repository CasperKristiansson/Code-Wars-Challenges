package main

import "fmt"

func FindOutlier(integers []int) int {
	var odd int = 0
	var even int = 0

	for i := 0; i < 3; i++ {
		if integers[i]%2 == 0 {
			even++
		} else {
			odd++
		}
	}

	for _, num := range integers {
		if (even > odd && num%2 != 0) || (odd > even && num%2 == 0) {
			return num
		}
	}

	return 0
}

func main() {
	fmt.Println("Running test")
	result := FindOutlier([]int{2, 6, 8, -10, 3})
	fmt.Println(result)
}
