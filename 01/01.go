package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var test_string string = `1721
979
366
299
675
1456`

func part1() {
	data, err := ioutil.ReadFile("01.txt")
	text := string(data)

	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	s := strings.Split(text, "\n")
	for i := 0; i < len(s); i++ {
		for j := 0; j < len(s); j++ {
			num1, _ := strconv.ParseInt(s[i], 10, 0)
			num2, _ := strconv.ParseInt(s[j], 10, 0)

			if num1+num2 == 2020 {
				solution := num1 * num2
				fmt.Println(solution)
			}
		}
	}
}

func part2() {
	data, err := ioutil.ReadFile("01.txt")
	text := string(data)

	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	s := strings.Split(text, "\n")
	for i := 0; i < len(s); i++ {
		for j := 0; j < len(s); j++ {
			for k := 0; k < len(s); k++ {
				num1, _ := strconv.ParseInt(s[i], 10, 0)
				num2, _ := strconv.ParseInt(s[j], 10, 0)
				num3, _ := strconv.ParseInt(s[k], 10, 0)

				if num1+num2+num3 == 2020 {
					solution := num1 * num2 * num3
					fmt.Println(solution)
				}
			}
		}
	}
}

func main() {
	part1()
	part2()
}
