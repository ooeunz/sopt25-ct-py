#1541 - 잃어버린 괄호

import sys

border = input().split('-')
result = 0
for i in range(len(border)):
    acc = sum(list(map(int, border[i].split('+'))))
    if i == 0:
        result += acc
    else:
        result -= acc
print(result)

