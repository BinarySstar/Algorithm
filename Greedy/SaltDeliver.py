n = int(input())

# box의 수
box = 0

while True:
    if (n % 5 == 0):
        box += n // 5
        print(box)
        break

    n = n - 3
    box += 1

    if (n < 0):
        print(-1)
        break
