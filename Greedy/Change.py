# 잔돈 리스트
coins = [500, 100, 50, 10, 5, 1]

# 결제한 지폐 1000엔
pay = 1000

# 결제할 금액
price = int(input())

# 거스름돈 계산
change = pay-price
result = 0

for coin in coins:
    result += change // coin
    change %= coin

print(result)
