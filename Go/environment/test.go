package main

import "fmt"

func FindOdd(seq []int) int {
	m := make(map[int]int)

	for _, num := range seq {
		if val, ok := m[num]; ok {
			m[num] = val + 1
		} else {
			m[num] = 1
		}
	}

	for key, value := range m {
		if value%2 != 0 {
			return key
		}
	}

	return 0
}

func main() {
	fmt.Println("Running test")
	result := Multiple3And5(10)
	fmt.Println(result)
}
