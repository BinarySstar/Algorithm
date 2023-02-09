T = int(input())

# 각 버튼의 조작 수의 리스트
time = [0, 0, 0]

# 버튼에 지정된 시간(단위 : 초)
button = [300, 60, 10]

for i in range(len(button)):
    time[i] = T // button[i]
    T %= button[i]

if (T != 0):  # 남은 시간이 0이 아니라면
    print(-1)
else:
    print(f"{time[0]} {time[1]} {time[2]}")
