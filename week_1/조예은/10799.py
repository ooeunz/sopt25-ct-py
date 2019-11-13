
bar = list(input())

rodNum = 0
sum = 0

for i in range(len(bar)):
    if bar[i] == '(':
        if bar[i+1] == ')':
            sum += rodNum
        else:
            rodNum += 1
            sum += 1
    elif bar[i] == ')':
        if bar[i-1] == '(':
            rodNum += 0
        else:
            rodNum -= 1

print(sum)
