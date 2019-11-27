grade = ['E','A','B','C','D']
result = list()

for _ in range(3):
    input_str = list(map(int,input().split()))
    result.append(grade[input_str.count(0)])

print("\n".join(map(str, result)))