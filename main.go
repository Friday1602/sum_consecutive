package main

import "fmt"

func main() {
	ast := "*"
	for i := 0; i < 5; i++ {
		fmt.Println(ast)
		ast += "*"
	}
}
