arr = input()
stack = []
answer = 0

for x in range(len(arr)):
    if arr[x] == "(":
        stack.append(x)
        last = arr[x]
    else:
        stack.pop()
        if last == "(":
            answer += len(stack)
            last = arr[x]
        else:
            #stack.pop()
            answer += 1

print(answer)

