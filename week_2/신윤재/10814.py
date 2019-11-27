length = int(input())
members = [list(input().split()) for _ in range(length)]

for i in range(length):
    members[i][0] = int(members[i][0])

members.sort(key=lambda n: n[0])

for member in members:
    print("{} {}".format(member[0], member[1]))