import sys
sys.stdin = open('input.숫자배열회전.txt')

#90도 회전
def degree_90(arr):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = arr[N-1-j][i]
    return result

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N*N 행렬
    N = int(input())
    arr = [list(map(str,input().split())) for _ in range(N)]

    # 90도 회전
    arr2 = degree_90(arr)
    # 90도 회전 + 90도 회전 = 180도 회전
    arr3 = degree_90(arr2)
    # 90도 회전 + 90도 회전 + 90도 회전 = 70도 회전
    arr4 = degree_90(arr3)
    print(f'#{tc}')
    for a,b,c in zip(arr2,arr3,arr4):
        a1 = ''.join(a)
        b1 = ''.join(b)
        c1 = ''.join(c)
        print(a1,b1,c1)