import sys
sys.stdin = open("sample_input_2.txt")

# T : 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # N : 정수의 개수, M : 구간의 개수
    N, M = map(int,input().split())
    # arr : N개의 정수
    arr = list(map(int,input().split()))

    # 가장 큰 합, 가장 작은 합
    resultmax = 0
    resultmin = 0
    
    for i in range(N-M+1):
        s = 0
        # M개씩의 합을 구하기
        for j in range(i,i+M):
            s += arr[j]

        # 가장 큰 합 구하기
        if s > resultmax:
            resultmax = s

        # 가장 작은 합 구하기
        # resultmin에 현재 0이 대입되어 있으므로 첫번째 s값 넣기
        if resultmin == 0:
            resultmin = s
        elif s < resultmin:
            resultmin = s

    print(f'#{tc} {resultmax - resultmin}')