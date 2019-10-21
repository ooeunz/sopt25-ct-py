length = int(input())

lst = [list(map(int, input().split())) for _ in range(length)]
lst = sorted(lst, key=lambda n: (n[1], n[0]))

for a, b in lst:
    print("{0} {1}".format(a, b))

