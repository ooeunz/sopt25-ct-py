# 정렬/ 백준 - 보물

cnt = int(input())
listA = input().split()
listB = input().split()

total_cnt = 0
listA.sort(reverse = True)

for each in range(cnt):
    maxB = max(listB)
    total_cnt += int(listA.pop()) * int(maxB)
    listB.remove(maxB)

print(total_cnt)