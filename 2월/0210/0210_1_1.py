import sys
sys.stdin = open('sample_input_1.txt')
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    # 가장 큰 수
    resultmax = arr[0]
    # 가장 작은 수
    resultmin = arr[0]
    for i in arr:
        if resultmax < i:
            resultmax = i
        if resultmin > i:
            resultmin = i

    result = resultmax - resultmin

    print(f'#{tc} {result}')
