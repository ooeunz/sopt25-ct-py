t = int(input())
dp = [0]*1000000
dp[0] = 1
dp[1] = 2
for i in range(2,t+1):
    dp[i] = ((dp[i-1]%15746) + (dp[i-2]%15746))%15746
print(dp[t-1])