def fibonacci(n):
    if n <= 0:
        return "Input should be positive"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1] + [0]*(n-2)
        for i in range(2, n):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[-1]
