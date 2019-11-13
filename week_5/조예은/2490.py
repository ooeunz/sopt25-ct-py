# 윷놀이 결과 출력

result = ['E', 'A', 'B', 'C', 'D']
zeroList = list()

for _ in range(3):
    wood = str(input().split(' '))
    zero = 0
    for i in wood:
        if i is '0':
            zero += 1
    zeroList.append(zero)

for num in zeroList:
    print(result[num])