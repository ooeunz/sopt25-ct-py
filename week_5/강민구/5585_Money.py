coins = [500, 100, 50, 10 , 5, 1]
value = int(input())
changes = 1000 - value
count = 0 # 최종적인 잔돈 갯수

for coin in coins :
    count += changes//coin # 거슬러줘야할 돈에서 동전 단위를 나눠서 갯수 추가
    changes = changes%coin # 동전 단위로 나눈 나머지를 입력 이는 곧 남은 잔돈이 된다
print(count)