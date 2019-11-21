# 책 페이즈 쪽수 번호 count
# 메모리초과 코드;;
count = [0 for _ in range(10)]
num = []

def solution(n):
    return None

n = int(input())
for i in range(1, n+1):
    num += list(str(i))

for i in num:
    word = int(i)
    count[word] += 1
print(' '.join(map(str, count)))