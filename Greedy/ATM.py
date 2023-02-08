# 사람 인원 수
n = input()

# 인출하는데 걸리는 시간
need_time = list(map(int, input().split()))

# 걸리는 시간을 오름차순으로 정리한다
need_time.sort()

result = 0
sum = 0

for i in range(len(need_time)):
    result += need_time[i]
    sum += result

print(sum)
