import sys

n = int(sys.stdin.readline().strip())
user_list = []

for _ in range(n):
    user_list.append(sys.stdin.readline().split())

user_list.sort(key= lambda user: int(user[0])) # sorted by age

print('\n'.join(map(lambda user: f'{user[0]} {user[1]}', user_list)))
