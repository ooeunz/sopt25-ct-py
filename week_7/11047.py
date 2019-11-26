coin_count,coin_sum = input().split()
coin_count = int(coin_count)
coin_sum = int(coin_sum)
coin_unit = []
result = 0
for _ in range(coin_count):
    coin_unit.append(int(input()))
for i in range(len(coin_unit)-1,-1,-1):
    while True:
        if(coin_unit[i]<=coin_sum):
            share = int(coin_sum/coin_unit[i])
            coin_sum = coin_sum - coin_unit[i]*share
            result = result + share
        elif(coin_unit[i]>coin_sum):
            break
    if(coin_sum == 0):
        break
print(result)