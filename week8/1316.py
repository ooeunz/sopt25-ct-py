# 1316 - 그룹단어체커

# 그룹단어란 각 문자가 연속해서 나타나는 경우

# 단어 중복이 연속이지 않을 경우 카운트 제외
# 반복문을 통해 현재 문자가 이전에 등장한 문자인지 확인


n = int(input())
answer = []
for i in range(n):
    word = list((input()))
    for j in range(len(word)):
        if j != len(word) - 1 and word[j] == word[j + 1]:
            pass
        elif word[j + 1:].count(word[j]) != 0:
            break
        elif j == len(word) - 1:
            answer.append(i)

print(len(answer))