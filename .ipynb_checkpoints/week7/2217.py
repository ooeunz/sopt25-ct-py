#2217-로프
#물체의 최대 중량을 구해내는 프로그램
# 내림차순으로 로프를 정렬한 뒤 (n번째 큰 수) * n 이 최대값


n = int(input())
rope =[]
for _ in range(n):
    rope.append(int(input()))
rope.sort()

result = 0
for i in range(n):
    result = max(result, rope[i] * (n-i))
print(result)
