T = int(input()) # 테스트 케이스 수
case =[]
for _ in range(T):
    N, M = list(map(int,input().split()))
    for _ in range(M):
        a,b = list(map(int,input().split()))
    case.append(N-1)
print(*case,sep='\n')
