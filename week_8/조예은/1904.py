# 01타일 문제 
# 타일 00,1로 만들 수 있는 타일 개수 구하기 
# 개수의 수를 풀어보면 피보나치 수열을 활용하는 문제

def solution(n):
    answer = 0
    a = 1
    b = 2

    for i in range(1, n+1):
        if i is 1: answer = a
        elif i is 2: answer = b
        else:
            answer = a + b
            a = b % 15746
            b = answer % 15746
    print(answer % 15746)

solution(int(input()))
