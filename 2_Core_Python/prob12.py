def longest_palindromic_substring(s):
    if not s or len(s) == 1:
        return s

    start, end = 0, 0

    for i in range(len(s)):
        # Odd length palindrome
        len1 = expand_from_center(s, i, i)
        # Even length palindrome
        len2 = expand_from_center(s, i, i + 1)

        max_len = max(len1, len2)

        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def expand_from_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1  # Final length of the palindrome

if __name__ == "__main__":
    test_strings = [
        "babad",  # "bab" or "aba"
        "cbbd",   # "bb"
        "a",      # "a"
        "ac",     # "a" or "c"
        "racecar" # "racecar"
    ]

    for s in test_strings:
        result = longest_palindromic_substring(s)
        print(f"Longest palindromic substring of '{s}' is '{result}'")