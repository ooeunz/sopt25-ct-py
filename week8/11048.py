#11048 - 이동하기
#최댓값

# 준규가(r, c)에 있으면, (r + 1, c), (r, c + 1), (r + 1, c + 1) = 오른쪽,아래, 오른쪽밑 대각선
# dp[i][j] = dp[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) = 반대로 왼쪽, 위, 왼쪽 위 대각선의 dp를 비교

import sys
n, m = map(int, input().split())
candy = []
for i in range(n):
    candy.append(list(map(int, input().split())))
dp = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = candy[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
print(dp[n][m])