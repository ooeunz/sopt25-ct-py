import sys

input = input()
result = 0
sum = 0

for i in range(len(input)):
    if input[i] == '(':          # (((
        sum += 1
    elif input[i] == ')':
        sum -= 1
        if input[i-1] == '(':  # ()레이저 쏘면 쌓인만큼 더하기
            result += sum
        else:                    # )))
            result += 1

print(result)