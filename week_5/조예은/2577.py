#  계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램

def solution(a, b, c):
    sen = str(a * b * c)
    count = [0 for _ in range(10)]
    for num in sen:
        count[int(num)] += 1
    for i in range(len(count)):
        print(count[i])    

if __name__ == "__main__":
    
    A = int(input())
    B = int(input())
    C = int(input())
    solution(A, B, C)