# 평균점수

x = 0
sum = 0
for each in range(5):
    x = int(input())
    if x < 40:
        x = 40
    sum += x
print(round(sum/5))