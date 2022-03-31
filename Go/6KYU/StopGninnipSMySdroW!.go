package main

import "strings"

func SpinWords(str string) string {
	words := strings.Fields(str)

	for index, word := range words {
		if len(word) >= 5 {
			words[index] = Reverse(word)
		}
	}

	return strings.Join(words, " ")
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
