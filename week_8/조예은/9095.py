# 1,2,3 더하기
# 직접 돌려보면 패턴 파악 가능
# 직전 세 개의 개수 더하면 됨

def solution(n):
    if n is 1: return 1
    elif n is 2: return 2
    elif n is 3: return 4
    else:
        return (solution(n-1) + solution(n-2) + solution(n-3))

answer = []
T = int(input())
for _ in range(T):
    answer.append(solution(int(input())))

for i in range(T):
    print(answer[i])
