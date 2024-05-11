package fibonacci

func FastFindFibonacciNum(num int) int {
	if num <= 1 {
		return num
	}
	a, b := 0, 1
	for i := 2; i <= num; i++ {
		a, b = b, a+b
	}
	return b
}

func RecursiveFindFibonacciNum(num int) int {
	if num <= 1 {
		return num
	}
	return RecursiveFindFibonacciNum(num-1) + RecursiveFindFibonacciNum(num-2)
}
