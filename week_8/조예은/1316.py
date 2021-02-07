# 연속된 문자가 있는 단어 찾기

answer = 0
N = int(input())
for _ in range(N):
    list_ = []
    word = list(input())
    for i in word:
        if i in list_ and i is not list_[-1]:
            break
        else:
            list_.append(i)
    if len(word) is len(list_):
       answer += 1
print(answer)
            
            
