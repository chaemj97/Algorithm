import sys
sys.stdin = open('sample_input.특별.txt')

# T : 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N : 정수의 개수, arr : N개의 정수
    N = int(input())
    arr = list(map(int,input().split()))

    # 특별히 정렬된 숫자를 10개까지만 출력할 것이니 10개만 만들기
    for i in range(0,10,2):
        # 큰 값 구해서 구간의 맨 앞으로
        max_v = i
        for j in range(i+1,N):
            if arr[max_v] < arr[j]:
                max_v = j
        arr[i], arr[max_v] = arr[max_v], arr[i]

        # 작은 값 구해서 큰 값 바로 뒤
        min_v = i+1
        for k in range(i+2,N):
            if arr[min_v] > arr[k]:
                min_v = k
        arr[i+1], arr[min_v] = arr[min_v], arr[i+1]

    print(f'#{tc}', *arr[0:10])