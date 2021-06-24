def longestPalindrome(s: str) -> str:
    # Dynamic Programming
    n = len(s)
    # Default to pick the first element if no palindrom found longer than 1
    longest, begin = 1, 0
    dp = [[None] * n for _ in range(n)]
    # All charactors itself is a palindrom:\
    for i in range(n):
        dp[i][i] = True
    # Try all possible substring lengths
    for length in range(2, n + 1):
        # Try all starting point
        for start in range(n):
            # Get ending index
            end = start + length - 1
            # Check if end index is larger than the total length
            if end >= n:
                break
            # s[start : end] will only be palindrom is the first and the last element is the same
            if s[start] != s[end]:
                dp[start][end] = False
            else:
                # s[start : end] will be a palendrom if [start + 1 : end - 1] is a panlindrom
                if length <= 2:
                    dp[start][end] = True
                else:
                    dp[start][end] = dp[start + 1][end - 1]
            # If s[start : end] is palindrom, compare the length with max length
            if dp[start][end]:
                if length > longest:
                    longest = length
                    begin = start
    return s[begin : begin + longest]


print(longestPalindrome("abcbaef"))