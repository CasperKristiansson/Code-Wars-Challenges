package main

import "fmt"

func IsTriangle(a, b, c int) bool {
	return a+b > c && a+c > b && b+c > a
}

func main() {
	fmt.Println("Running test")
	result := IsTriangle(3, 1, 5)
	fmt.Println(result)
}
