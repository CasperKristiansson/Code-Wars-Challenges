package main

import "fmt"

func PrinterError(s string) string {
	var count int

	for _, v := range s {
		if v > 'm' {
			count++
		}
	}

	return fmt.Sprintf("%d/%d", count, len(s))
}

func main() {
	fmt.Println("Running test")
	result := PrinterError("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
	fmt.Println(result)
}
