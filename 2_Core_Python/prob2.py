def get_permutations(s):
    # Base case: only one character
    if len(s) == 1:
        return [s]

    perms = []  # Store all permutations
    for i in range(len(s)):
        # Fix one character and find permutations of the remaining
        fixed_char = s[i]
        remaining = s[:i] + s[i+1:]
        for sub_perm in get_permutations(remaining):
            perms.append(fixed_char + sub_perm)

    return perms

# Example usage
if __name__ == "__main__":
    input_str = "Bharath"
    result = get_permutations(input_str)
    print(f"All permutations of '{input_str}':")
    for perm in result:
        print(perm)