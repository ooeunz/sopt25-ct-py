# 그리디 알고리즘 - 잃어버린 괄호
# 숫자가 0부터 시작할 수 있는 것을 고려해야 하기 때문에 eval사용 X 
# int 로 변환하여 sum 사용 
# -를 기준으로 split한 다음 +로 split한 값을 정수화 후 sum
# sum 이후에도 따로 있는 값은 -이므로 빼줌

n = [sum(int(x) for x in y.split('+')) for y in input().split('-')]
print(n[0] - sum(n[1:]))
