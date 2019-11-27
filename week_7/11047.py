import sys

def calculator(wallet : list, money : int):
    count = 0
    for w in wallet:
        div = money // w
        if div:
            count += div
            money = money % w

        if not money:
            return count



if __name__ == "__main__":
    n, money = map(int, sys.stdin.readline().split())
    wallet = []
    for _ in range(n):
        wallet.append(int(sys.stdin.readline()))
    wallet.reverse()

    print(calculator(wallet, money))
