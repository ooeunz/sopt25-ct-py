total = int(input())
people = list(map(int,input().split()))
people.sort()

sum = 0

for idx, value in enumerate(people):
    sum += value * (total - idx)

print(sum)