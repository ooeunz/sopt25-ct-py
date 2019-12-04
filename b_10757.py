a, b = tuple(input().split())
a = a[::-1] # reverse str
b = b[::-1] # reverse str
prop = 0

t = max(len(a), len(b)) + 1
result = list()

for cur in range(t):
    ap = int(a[cur]) if len(a) > cur else 0
    bp = int(b[cur]) if len(b) > cur else 0
    calc = ap + bp + prop
    if cur == t-1 and calc == 0:
        break
    result.append(calc%10)
    prop = int(calc/10)

result.reverse()
print(''.join(map(str, result)))
