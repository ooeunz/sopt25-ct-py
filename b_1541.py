ip = [sum(map(int, exp.split('+'))) for exp in input().split('-')]
print(ip[0] - sum(ip[1:]))