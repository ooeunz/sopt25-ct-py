# 재귀로 팩토리얼 풀기

def solution(num):
    return num * solution(num-1) if num > 1 else 1

if __name__ == "__main__":
    num = int(input())
    print(solution(num))