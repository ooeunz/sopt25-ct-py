ip = [input() for _ in range(int(input()))]

cnt=0

for word in ip:
    prv = word[0]
    don = [prv]
    flag = True
    for c in word[1:]:
        if prv == c:
            continue
        elif c in don:
            flag = False
            break
        else:
            don.append(c)
        prv = c
    if flag:
        cnt = cnt+1

print(cnt)