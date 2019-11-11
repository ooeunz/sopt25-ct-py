phone = {' ':[1,0],'A':[2,0],'B':[2,1],'C':[2,2],'D':[3,0],'E':[3,1],'F':[3,2],
        'G':[4,0],'H':[4,1],'I':[4,2],
        'J':[5,0],'K':[5,1],'L':[5,2],'M':[6,0],'N':[6,1],'O':[6,2],
        'P':[7,0],'Q':[7,1],'R':[7,2],'S':[7,3],
        'T':[8,0],'U':[8,1],'V':[8,2],'W':[9,0],'X':[9,1],'Y':[9,2],'Z':[9,3]}
p,w = input().split(" ")
p = int(p)
w = int(w)
result = 0
message = list(input())
before_button = [-1,-1]
for i in message:
    now_button = phone[i]
    if(before_button[0] == now_button[0]):
        result = result + (now_button[1]+1)*p + w
    else:
        result = result + (now_button[1]+1)*p
    if(now_button[0]==1):
        before_button = [-1,-1]
    else:
        before_button = now_button
print(result)