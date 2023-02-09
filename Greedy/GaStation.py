# 도시의 개수 N
N = int(input())

# 도시 간 거리 리스트
distance = list(map(int, input().split()))

# 리터 당 가격 리스트
oil = list(map(int, input().split()))

# 리터 당 최저비용, 첫 번째 주유소에서는 무조건 주유
lowest = oil[0]

# 누적 거리
cDistance = distance[0]

# 최저비용
price = 0

# 리터 당 가격이 싼 주요소에서 최대한 많이 주유
for i in range(1, N-1):
    if (lowest >= oil[i]):
        price += lowest * cDistance
        lowest = oil[i]
        cDistance = 0
    cDistance += distance[i]

# 마지막 거리까지 더해주기
price += lowest * cDistance

print(price)
