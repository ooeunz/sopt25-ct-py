count = int(input())
rope = []
for _ in range(count):
    rope.append(int(input()))
rope.sort()
rope.reverse()
result = 0
for i in range(len(rope)):
    if((i+1)*rope[i]>result):
        result = (i+1)*rope[i]
print(result)