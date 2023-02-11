String = input()
count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

# 첫 번째 원소 비교
if (String[0] == '0'):
    count1 += 1
else:
    count0 += 1

# 모든 원소를 비교한다
for i in range(len(String)-1):
    if (String[i] != String[i+1]):
        if (String[i+1] == '0'):
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))
