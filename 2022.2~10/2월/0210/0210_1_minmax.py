import sys
sys.stdin = open('sample_input_1.txt')
T = int(input())

def maxmin(ls):
    # 가장 큰 수
    resultmax = ls[0]
    # 가장 작은 수
    resultmin = ls[0]
    for i in ls:
        if resultmax < i:
            resultmax = i
        if resultmin > i:
            resultmin = i

    return resultmax - resultmin

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    result = maxmin(arr)

    print(f'#{tc} {result}')
