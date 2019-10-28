size = input()
first = []
second = []
first = input().split()
second = input().split()
first = list(map(int, first))
second = list(map(int, second))
first.sort()
second.sort()
second.reverse()
result = 0
for i in range(0,len(first)):
    result = result + first[i]*second[i]
print(result)