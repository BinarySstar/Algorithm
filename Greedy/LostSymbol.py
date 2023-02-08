# 식을 모두 문자열 리스트로 입력받기, - 기호를 기준으로 split
formula = list(map(str, input().split('-')))

intList = []
# 원소 중에 + 기호가 포함되어 있으면 split 하고 더해 formula 리스트에 추가
for i in formula:
    tmpSum = 0
    if ('+' in i):
        tmpSum = sum(list(map(int, i.split('+'))))
        intList.append(tmpSum)
    else:
        intList.append(int(i))  # 정수형으로 바꿔주고 intList에 추가


# 첫 번째와 마지막은 숫자인 조건을 이용하여 모두 빼기
result = intList[0]
for i in range(1, len(intList)):
    result -= intList[i]

print(result)
