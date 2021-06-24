def getUmbrellas(requirement, sizes):
    
    dp = [float('inf')] * (requirement + 1)
    dp[0] = 0
    
    for size in sizes:
        for i in range(size, requirement + 1):
            dp[i] = min(dp[i], dp[i - size] + 1) # we have to compute all minimum counts for requirement up to i. 

    if dp[requirement] != float('inf'):
        return dp[requirement]
    else:
        return -1
    
print(getUmbrellas(8,[3,5]))