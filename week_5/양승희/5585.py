# 거스름돈

import math

change = 1000 - int(input())
money = [500,100,50,10,5,1]
totalCnt = 0

for each in money:
    if (change/each) >= 1 :
        eachCnt = math.floor(change/each)
        
        totalCnt += eachCnt
        change = change - each*eachCnt

print(totalCnt)