def max_subarray_sum(arr):
    if not arr:
        return 0

    max_current = max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current

    return max_global


# 🔍 Example usage
if __name__ == "__main__":
    test_arrays = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-5, -1, -8, -9],
        [3, -2, 5, -1],
        [],
    ]

    for arr in test_arrays:
        result = max_subarray_sum(arr)
        print(f"Max subarray sum of {arr} is {result}")