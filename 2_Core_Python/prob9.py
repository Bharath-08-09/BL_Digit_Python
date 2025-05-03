def sqrt_binary_search(x, precision=1e-6):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")

    if x == 0 or x == 1:
        return x

    low = 0
    high = x if x >= 1 else 1  # Handle numbers < 1
    mid = (low + high) / 2

    while abs(mid * mid - x) > precision:
        if mid * mid < x:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2

    return mid


# 🔍 Example usage
if __name__ == "__main__":
    test_numbers = [25, 2, 0.25, 0, 1, 10]
    for num in test_numbers:
        result = sqrt_binary_search(num)
        print(f"Square root of {num} ≈ {result:.6f}")