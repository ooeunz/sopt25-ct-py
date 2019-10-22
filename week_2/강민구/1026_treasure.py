T = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0

a.sort()

for i in range(len(a)) :
    result += a[i]*max(b)
    b.remove(max(b))

print(result)

