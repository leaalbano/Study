package main

import (
	"fmt"

	"example.com/greeting"
)

func main() {
	// Get a greeting message and print it.
	message := greeting.Hello("Lea")
	fmt.Println(message)
}
