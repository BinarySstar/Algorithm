# 동전 종류의 수와 금액
n, k = map(int, input().split())

# 동전 단위금액이 들어갈 리스트 생성
coins = []

# k 만큼 만들 수 있는 동전의 개수
count = 0

# n 만큼 입력받고 coins 리스트에 추가하기
for i in range(n):
    a = int(input())
    coins.append(a)

# 리스트 내림차순으로 정렬
coins.sort(reverse=True)

# 해당 화폐로 만들 수 있는 동전의 개수 세기
for coin in coins:
    count += k // coin
    k %= coin

print(count)
