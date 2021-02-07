# 그리디 알고리즘 - 동전 가능한 동전매수

import sys
answer = 0
value = []
N, K = map(int, sys.stdin.readline().split())
for _ in range(N):
    value.append(int(input()))
value.sort(reverse=True)

for i in value:
    if K >= i and K > 0:
        answer += int(K / i)
        K -= int(K/i)*i
print(answer)