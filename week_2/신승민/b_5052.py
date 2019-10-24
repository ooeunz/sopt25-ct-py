import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = sorted(list(sys.stdin.readline().strip() for _ in range(n)))
    result = not list(filter(lambda bo: bo,map(lambda pair: pair[1].startswith(pair[0]) , zip(l[:-1], l[1:]))))
    print('YES' if result == True else 'NO')
