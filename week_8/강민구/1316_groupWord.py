N = int(input())
result = 0
for _ in range(N):
    word = input()
    check = []
    for index,alpha in enumerate(word) :
        if index == 0 :
            check.append(alpha)
        else :
            if alpha == word[index-1] or alpha not in check :
                if alpha not in check :
                    check.append(alpha)
            else :
                break
        if index == len(word)-1 :
            result += 1
print(result)