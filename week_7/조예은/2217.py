# 그리디 알고리즘 - 로프 중량
# 로프를 모두 사용하지 않아도 되므로, 
# 정렬해서 가장 작은 수로 전체 로프를 다 사용할때부터 
# 가장 큰 수로 한 개의 로프만 사용할때까지를 검사하여 max값 출력

answer = 0
N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()
for i in range(N):
    answer = max((N-i) * ropes[i], answer)
print(answer)

