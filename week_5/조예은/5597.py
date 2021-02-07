# 출석번호 받아서 과제 안 낸 번호 솎아내기
student = [0] * 30
for i in range(28):
    num = int(input())
    student[num-1] = 1

for i in range(len(student)):
    if student[i] is 0:
        print(i+1)