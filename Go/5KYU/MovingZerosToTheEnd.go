package main

func MoveZeros(arr []int) []int {
	var index int = 0
	var stop int = len(arr)

	for index < stop {
		if arr[index] == 0 {
			(arr) = append((arr)[:index], append((arr)[index+1:], []int{0}...)...)
			stop -= 1
		} else {
			index += 1
		}
	}

	return arr
}
