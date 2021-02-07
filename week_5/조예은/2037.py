# 문자메세지 소요시간 계산
SHORT_PUSH, LONG_PUSH = map(int, input().split(' '))
sentence = list(input())
result = 0

for i in range(len(sentence)):
    # A, B, C
    if 65 <= ord(sentence[i]) <= 67:
        result += (ord(sentence[i])-64) * SHORT_PUSH
        if i is not 0 and 65 <= ord(sentence[i-1]) <= 67:
            result += LONG_PUSH
     # D, E, F
    elif 68 <= ord(sentence[i]) <= 70:
        result += (ord(sentence[i])-67) * SHORT_PUSH
        if i is not 0  and 68 <= ord(sentence[i-1]) <= 70:
            result += LONG_PUSH
     # G, H, I
    elif 71 <= ord(sentence[i]) <= 73:
        result += (ord(sentence[i])-70) * SHORT_PUSH
        if i is not 0 and 71 <= ord(sentence[i-1]) <= 73:
            result += LONG_PUSH
     # J, K, L
    elif 74 <= ord(sentence[i]) <= 76:
        result += (ord(sentence[i])-73) * SHORT_PUSH
        if i is not 0 and 74 <= ord(sentence[i-1]) <= 76:
            result += LONG_PUSH
     # M, N, O
    elif 77 <= ord(sentence[i]) <= 79:
        result += (ord(sentence[i])-76) * SHORT_PUSH
        if i is not 0 and 77 <= ord(sentence[i-1]) <= 79:
            result += LONG_PUSH
     # P, Q, R, S
    elif 80 <= ord(sentence[i]) <= 83:
        result += (ord(sentence[i])-79) * SHORT_PUSH
        if i is not 0 and 80 <= ord(sentence[i-1]) <= 83:
            result += LONG_PUSH
     # T, U, V
    elif 84 <= ord(sentence[i]) <= 86:
        result += (ord(sentence[i])-83) * SHORT_PUSH
        if i is not 0 and 84 <= ord(sentence[i-1]) <= 86:
            result += LONG_PUSH
     # W, X, Y, Z
    elif 87 <= ord(sentence[i]) <= 90:
        result += (ord(sentence[i])-86) * SHORT_PUSH
        if i is not 0 and 87 <= ord(sentence[i-1]) <= 90:
            result += LONG_PUSH
    else:
        result += SHORT_PUSH
print(result)