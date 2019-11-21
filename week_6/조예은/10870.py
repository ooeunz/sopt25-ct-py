# 피보나치 수열 재귀

def solution(num):
    return solution(num-1) + solution(num-2) if num>1 else num

if __name__ == "__main__":
    num = int(input())
    print(solution(num))