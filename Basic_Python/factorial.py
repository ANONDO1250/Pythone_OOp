def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = 5  # Change this to the desired number
factorial_result = factorial(number)
print(f"The factorial of {number} is: {factorial_result}")
