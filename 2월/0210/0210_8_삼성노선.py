# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # 버스 노선의 개수
    N = int(input())
    # 5001개의 버스 정류장
    arr = [0] * 5001
    # 지나가는 버스 정류장에 1 추가 (idx 주의)
    for i in range(N):
        A, B = map(int,input().split())
        for j in range(A,B+1):
            arr[j] += 1

    # 출력해야하는 P개의 정류장, 각각의 idx의 해당하는 값을 result에 넣기
    P = int(input())
    result = [0] * P
    for k in range(P):
        C = int(input())
        result[k] = arr[C]

    print(f'#{tc}',*result)