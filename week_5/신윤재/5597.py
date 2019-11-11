attendance = [False] * 30
for _ in range(28):
    student = int(input())
    attendance[student-1] = True
for idx, stu in enumerate(attendance):
    if not stu:
        print(idx+1)