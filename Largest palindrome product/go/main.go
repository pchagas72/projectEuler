package main

import (
	"bytes"
	"strconv"
	"strings"
)

func reverseString(product string) string {
	var out bytes.Buffer
	for i := len(product) - 1; i >= 0; i-- {
		out.WriteByte(product[i])
	}
	return out.String()
}

func checkPalindromic(product string) bool {
	var half_length_string string = strconv.Itoa(len(product))
	if strings.Contains(half_length_string, ".") {
		return false
	} else {
		if product == reverseString(product) {
			return true
		}
	}
	return false
}

func solve() int {
	var largest = 0
	for i := 999; i >= 100; i-- {
		for k := 999; k >= 100; k-- {
			var product int = i * k
			if checkPalindromic(strconv.Itoa(product)) {
				if product >= largest {
					largest = product
				}
			}
		}
	}
	return largest
}

func main() {
	println(solve())
}
