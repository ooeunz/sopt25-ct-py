# 거스름돈 매수

remoney = 1000 - int(input())
moneyList = [500, 100, 50, 10, 5, 1]
sum = 0

for ann in moneyList:
    if remoney > 0:
        type = int(remoney/ann)
        sum += type
        remoney -= type * ann
print(sum)