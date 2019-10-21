import sys


def solution(phone_number):
    for i in range(len(phone_number)-1):
        if phone_number[i+1].startswith(phone_number[i]):
            return "NO"
    return 'YES'

if __name__ == "__main__":
    time = int(sys.stdin.readline())
    for _ in range(time):
        n = int(sys.stdin.readline())
        phone_number = sorted(list(sys.stdin.readline().strip() for _ in range(n)))
        print(solution(phone_number))