import sys

n = int(sys.stdin.readline())
a = [0] * 10001

for _ in range(n):
    value = int(sys.stdin.readline())
    a[value] += 1

for i in range(10001):
    if a[i] > 0:
        print(f'{i}\n'*a[i], end="")