OPEN = "("
CLOSE = ")"
def solution(brackets):
    check = 0
    for bracket in brackets:
        if bracket == OPEN:
            check += 1
        elif bracket == CLOSE:
            check -=1
        if check<0:
            return "NO"
    if check == 0:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    K = int(input())
    for k in range(K):
        brackets = input()
        print(solution(brackets))