# 11399 - ATM

#시간이 가장 짧게 걸리는 순부터 많이 걸리는 순서대로 배열
import sys

n = int(input())
arr = list(map(int, input().split()))

# if n == 1:  # 1
#     print(arr[0])
# else:
arr.sort()  # 2

i_sum = 0
min_sum = 0

for i in range(n):
    min_sum += (i_sum + arr[i])  # 3
    i_sum += arr[i]  # 4

print(min_sum)


#if문 뺐더니 됨 실화냐

