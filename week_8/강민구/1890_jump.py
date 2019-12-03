N = int(input())
jump_map = [[int(n) for n in input().split()] for _ in range(N)] # 점프맵 생성
dp = [[0 for _ in range(N)] for _ in range(N)] # dp맵 생성
dp[0][0] = 1 #dp 초기값에 1을 넣어줌으로써 경우의 수 시작
for i in range(N) :
    for j in range(N) :
        if i == N-1 and j == N-1 :
            break
        jump = jump_map[i][j]
        ax = i + jump
        ay = j + jump
        # 다음 도착지에 현재 위치까지 오는 경우의 수를 저장
        if ax < N :
            dp[ax][j] += dp[i][j]
        if ay < N :
            dp[i][ay] += dp[i][j]
print(dp[-1][-1])
########## dfs로 풀때
# stack = [] #dfs를 위한 스택
# result = 0 #최종 경우의 수
# stack.append((0,0)) # 시작점 설정
#
# #dfs 시작
# while stack :
#     x,y = stack.pop()
#     if jump_map[x][y] == 0 :
#         result += 1
#     else :
#         ax = x + jump_map[x][y]
#         ay = y + jump_map[x][y]
#
#         if ax > 0 and ax < N :
#             stack.append((ax,y))
#         if ay > 0 and ay < N :
#             stack.append((x, ay))
# print(result) # 최종 결과 출력