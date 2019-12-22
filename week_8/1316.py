count = int(input())
words = []
for _ in range(count):
    words.append(input())
result = []
answer = 0
for i in range(count):
    compare = '-'
    for j in range(len(words[i])):
        if(words[i][j] is not compare):
            if(words[i][j] in result):
                break
            result.append(words[i][j])
            compare = words[i][j]
        else:
            pass
        if(j==(len(words[i])-1)):
            answer = answer + 1
    result = []
print(answer)