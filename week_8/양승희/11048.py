N, M = map(int, input().split(' '))
maze = list()
dp = list()

for i in range(N):
    maze.append(list(map(int,input().split())))
    dp.append([0 for i in range(M)])

for i in range(N) :
    for j in range(M):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        dp[i][j] += maze[i][j]

print(dp[N-1][M-1])