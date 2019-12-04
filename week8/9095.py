# 9095 - 1,2,3 더하기

#  1의개수, 2의개수, 3의 개수를 다더해주면 4의개수가 됨
#  ex) 10의 개수는 (7,8,9의 개수를 다 더한것)

n = int(input())
core = [1, 2, 4]
for i in range(3, 10):
    core.append(core[i - 3] + core[i - 2] + core[i - 1])
for _ in range(n):
    k = int(input())
    print(core[k - 1])

