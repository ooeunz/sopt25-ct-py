def solution():
    square = list(map(int, input().split()))
    square.sort(reverse=True)

    square[1], square[2] = square[2], square[1]

    width = square[0] if square[0] < square[2] else square[2]
    heigth = square[1] if square[1] < square[3] else square[3]

    print(width * heigth)

if __name__ == "__main__":
    solution()