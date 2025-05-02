def fibonacci(n):
    if n <= 0:
        return "❌ Input must be a positive integer"
    elif n == 1:
        return 0  # First Fibonacci number
    elif n == 2:
        return 1  # Second Fibonacci number
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    n = 5
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")