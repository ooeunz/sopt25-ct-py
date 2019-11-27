days = int(input())
time_table = list()
for _ in range(days):
    time_table.append(tuple(map(int, input().split(' '))))

time_table.sort(key=lambda x: x[0], reverse=True)

for day in reversed(range(1, days+1)):
    possible = [(dead, carrot) for dead, carrot in time_table if dead >= day]