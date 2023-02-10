# 테스트 케이스의 수 T
T = int(input())

for _ in range(T):
    score = []
    N = int(input())  # 지원자 숫자 N
    for _ in range(N):
        n, m = map(int, input().split())  # 점수 입력받아 리스트에 추가
        score.append([n, m])

    # 서류 전형 기준으로 오름차순 정렬
    score.sort()
    result = 1

    # 면접 점수로 비교하기
    highest = score[0][1]

    # 가장 점수가 높은 것과 비교하기
    for i in range(N):
        if (highest > score[i][1]):
            highest = score[i][1]
            result += 1

    print(result)
