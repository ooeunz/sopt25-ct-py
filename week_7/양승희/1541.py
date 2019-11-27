import sys

express = sys.stdin.readline().split('-')
result = 0

for idx,value in enumerate(express):
    inner_express = list(map(int,value.split('+')))
    if idx == 0:
        result += sum(inner_express)
    else:
        result -= sum(inner_express)

print(result)