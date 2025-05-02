def longest_common_subsequence(X, Y):
    m, n = len(X), len(Y)
    
    # Create a 2D DP table initialized with 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS string from the DP table
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

# Example usage
if __name__ == "__main__":
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    result = longest_common_subsequence(str1, str2)
    print(f"Longest Common Subsequence: {result}")