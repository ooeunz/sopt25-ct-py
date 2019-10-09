##백준 10799 '레이저'
arrangement = input()
answer = 0
stack = []
for i in range(len(arrangement)):
    if arrangement[i] == '(':
        stack.append('(')

    else:
        stack.pop()
        if arrangement[i - 1] == '(':
            answer += len(stack)
        else:
            answer = answer + 1
print(answer)