# 자연수 S
S = int(input())

# 자연수 판별
if (S <= 0):
    pass
else:
    # 자연수 i와 자연수를 세는 count 변수
    i = 1
    count = 0
    while (S-i >= i+1):
        S -= i
        i += 1
        count += 1
    count += 1  # 마지막 경우까지 더한다
    print(count)
