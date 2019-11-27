kinds, total_money = map(int,input().split())
money_kinds = list() 
cnt = 0

for _ in range(kinds):
    money_kinds.append(int(input()))

money_kinds.sort(reverse =True)
for value in money_kinds:
    quot = (total_money // value)
    if quot >= 1 :
        cnt += quot
        total_money -= quot * value

print(cnt)