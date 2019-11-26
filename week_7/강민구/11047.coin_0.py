import sys

N, K = map(int,input().split())
coins = list(sys.stdin.readline().strip() for _ in range(N))
coins = list(map(int,coins))
coins.sort(reverse=True)
answer = 0
for coin in coins :
    if(K >= coin) :
        answer += K//coin
        K = K%coin
print(answer)