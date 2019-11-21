
def hanoi(num, A, B, C):
    if num is 1:
        print(A, C)
    else:
        hanoi(num-1,A, C, B)
        print(A, C)
        hanoi(num-1,B, A, C)

if __name__ == "__main__":
    plate = int(input())
    print(pow(2, plate)-1)
    hanoi(plate, '1', '2', '3')