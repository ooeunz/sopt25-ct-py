OPEN = "("
CLOSE = ")"

def solution(irons):
    # initialization
    stack = []
    ans = 0
    irons = irons.replace("()", "l")

    for iron in irons:
        if iron == OPEN:
            stack.append(iron)
        elif iron == CLOSE:
            stack.pop()
            ans += 1
        elif iron == "l":
            ans += len(stack)
    return ans

if __name__ == "__main__":
    irons = input()
    print(solution(irons))