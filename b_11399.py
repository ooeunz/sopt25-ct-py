n = int(input())
ip = sorted([int(i) for i in input().split(' ')])
sum = 0
for i in range(n):
    sum += (n-i)*ip[i]
print(sum)