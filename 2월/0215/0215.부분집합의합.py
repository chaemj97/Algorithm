# T : 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # N : 부분 집합 원소의 개수, K : 부분 집합 원소의 총 합
    N, K = map(int,input().split())

    # 1~ 12까지 숫자를 원소로 가진 집합
    arr = [i for i in range(1,13)]
    # 부분 집합의 원소의 개수가 N, 부분 집합 원소의 총 합이 K인 부분집합 개수
    result = 0

    # 모든 부분 집합 확인
    for i in range(1<<12):
        # 부분집합의 합
        sum_sub = 0
        # 부분집합
        subset = []
        for j in range(12):
            if i & (1<<j):
            # j번째 요소는 부분집합에 포함
                sum_sub += arr[j]
                subset.append(arr[j])

    # 부분 집합의 원소의 개수가 N, 부분 집합 원소의 총 합이 K인 부분집합 개수 구하기
        if len(subset) == N and sum_sub == K:
            result += 1

    print(f'#{tc} {result}')