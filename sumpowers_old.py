"""
*** This code is the old version. Please refer to sumpowers.py for new version.
Given two numbers X and N
We find __"number of ways"__ X can be expressed as:
sum of n-th power of unique natural numbers.
"""
x = 738     
n = 3 

dp = [1] + [0] * x

for i in range(1, int(pow(x, 1 / n)) + 1):
    u = i ** n
    for j in range(x, u - 1, -1):
        dp[j] += dp[j - u]
print(dp[-1])
