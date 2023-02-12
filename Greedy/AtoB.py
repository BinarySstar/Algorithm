a, b = map(int, input().split())
count = 1

while (b != a):
    count += 1
    temp = b
    if (b % 10 == 1):  # 끝 자리가 1이라면
        b //= 10
    elif (b % 2 == 0):
        b //= 2

    if (temp == b):
        count = -1
        break

print(count)
