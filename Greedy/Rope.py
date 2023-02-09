# 로프의 개수 k
N = int(input())

ropeWeight = []

# 한 줄씩 입력받아 리스트에 저장
for _ in range(N):
    a = int(input())
    ropeWeight.append(a)

# 중량을 오름차순으로 정렬
ropeWeight.sort()

# 최대 중량 maximum, 로프를 1개만 사용할 때는 최댓값이 곧 최대 중량
maximum = ropeWeight[-1]

for i in range(2, N+1):
    ropeWeight.pop()  # 최댓값을 없애주기
    if (maximum < ropeWeight[-1] * i):
        maximum = ropeWeight[-1] * i


print(maximum)
