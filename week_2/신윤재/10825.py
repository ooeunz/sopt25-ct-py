def solution():
    N = int(input())
    # students = [["Junkyu", "50", "60", "100"], ["Sangkeun", "80", "60", "50"], ["Sunyoung", "80", "70", "100"], ["Soong", "50", "60", "90"], ["Haebin", "50", "60", "100"], ["Kangsoo", "60", "80", "100"], ["Donghyuk", "80", "60", "100"], ["Sei", "70", "70", "70"], ["Wonseob", "70", "70", "90"], ["Sanghyun", "70", "70", "80"], ["nsj", "80", "80", "80"], ["Taewhan", "50", "60", "90"]]
    students = [list(input().split()) for _ in range(N)]
    for i in range(N):
        students[i][1] = int(students[i][1])
        students[i][2] = int(students[i][2])
        students[i][3] = int(students[i][3])

    ans = sorted(students, key=lambda n: (-n[1], n[2], -n[3], n[0]))
    for a in ans:
        print(a[0])

if __name__ == "__main__":
    solution()