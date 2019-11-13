import sys
T = int(input())
person = list(sys.stdin.readline().strip() for _ in range(T))
person = list(map(int,person))
result = 0
stack = [] # 서있는 사람들의 키를 저장
same_person = [] # 같은 키의 사람이 몇 명인지 확인
for i in person :
    count = 1
    while stack and stack[-1] <= i :
        result += same_person[-1]
        if stack[-1] == i : # 같은 키가 들어왔을 경우
            count += same_person[-1] #count 값에 같은 키가 몇명 붙어 있는지 저장(새로 들어온 사람까지 합쳐서)
        stack.pop()
        same_person.pop()

    if stack :
        result += 1

    stack.append(i)
    same_person.append(count) #연속 몇명인지 갱신

print(result)
