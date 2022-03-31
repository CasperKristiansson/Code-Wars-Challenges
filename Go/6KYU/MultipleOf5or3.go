package main

import "fmt"

func Multiple3And5(number int) int {
	var sum int = 0

	for i := 0; i < number; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}

	return sum
}

func main() {
	fmt.Println("Running test")
	result := Multiple3And5(10)
	fmt.Println(result)
}
