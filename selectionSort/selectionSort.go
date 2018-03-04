package main

import "fmt"

// Selection Sort Algorithm

func selectionSort(arr []int) {
	for i := range arr {
		var tar = i
		for j := i + 1; j < len(arr); j++ {
			if arr[tar] > arr[j] {
				tar = j
			}
		}
		arr[i], arr[tar] = arr[tar], arr[i]
	}
	fmt.Printf("Sorted Array: %v\n", arr)
}

func main() {
	arr := []int{100, 432, 431, 5743, 783, 89, 4234, 52, 76}
	selectionSort(arr)
}
