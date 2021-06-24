from pprint import pprint


def longestPalindrome(s):
    
    dp = [[None] * len(s) for _ in range(len(s))]
    begin = 0
    longest = 1
    # all single letter are palindrome
    for i in range(len(s)):
        dp[i][i] = True

    # building palindrome from 2 letter onwards from left to right    
    for length in range(2, len(s) + 1):
        
        # trying all starting point
        for start in range(len(s)):
            end = start + length - 1
            
            if end > (len(s) - 1):
                break
            
            if s[start] != s[end]:
                dp[start][end] = False
            
            else:
                if length == 2:
                    dp[start][end] = True
                
                else:
                    dp[start][end] = dp[start+1][end-1]
            
            if dp[start][end]:
                if length > longest:
                    longest = length
                    begin = start
    return s[begin : begin + longest]  
        
        

    
print(longestPalindrome("abcdefokfoksefdsfasdf"))