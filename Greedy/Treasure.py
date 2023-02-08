# 배열의 길이 N
n = int(input())

# 배열 A, B 입력받기
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

# 함수 S의 값
sum = 0

# 배열 A의 최솟값과 배열 B의 최댓값을 곱한 후, 해당 값 삭제
for _ in range(n):
    a = min(arrayA)
    b = max(arrayB)
    sum += (a * b)

    arrayA.remove(a)
    arrayB.remove(b)

print(sum)
