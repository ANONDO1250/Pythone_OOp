def generate_fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series


n = 10  # Change this to the desired number of Fibonacci numbers
fibonacci_series = generate_fibonacci(n)
print(f"Fibonacci Series: {fibonacci_series}")
