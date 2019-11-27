# 11047 - 동전0

# k보다 작은것 중 가장 큰 값부터 계산함
# k와 값을 나눈 몫을 계속 더해주고 k에는 값을 나눈 나머지를 저장


# n = 입력 개수, k는 금액

n, k = map(int, input().split())
coin = []
result = 0

for i in range(n):
    coin.append(int(input()))

for i in range(1, n + 1):
    # 인덱스 끝부터 순회 : coin[-i] 마이너스 인덱스
    if k // coin[-i] > 0:
        result += k // coin[-i]
        k = k % coin[-i]
        if k == 0:
            break

print(result)
