people = int(input())
agreement = 0

for _ in range(people):
    vote = int(input())
    if vote:
        agreement += 1

print("Junhee is not cute!" if (people - agreement) > agreement else  "Junhee is cute!")