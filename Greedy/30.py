N = str(input())

result = 0

# N에 0이 없으면 -1 출력
if ('0' not in N):
    result = -1
else:
    # 수를 모두 더한 값이 3의 배수가 나오는지 확인
    sumOfNumber = 0
    for i in range(len(N)):
        sumOfNumber += int(N[i])

    if (sumOfNumber % 3 != 0):
        result = -1

    else:
        # N을 내림차순으로 정렬하고 정수로 바꾼다
        number = sorted(N, reverse=True)
        result = int("".join(number))

print(result)
