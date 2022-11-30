import sys
sys.stdin = open('input.숫자배열회전.txt')

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N*N 행렬
    N = int(input())
    arr1 = [list(map(str,input().split())) for _ in range(N)]
    # 90도 회전
    arr2 = [[0]*N for _ in range(N)]
    # 180도 회전
    arr3 = [[0] * N for _ in range(N)]
    # 270도 회전
    arr4 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr1[N-1-j][i]
            arr3[i][j] = arr1[N-1-i][N-1-j]
            arr4[i][j] = arr1[j][N-1-i]
    print(f'#{tc}')
    for a1,a2,a3 in zip(arr2,arr3,arr4):
        a11 = ''.join(a1)
        a22 = ''.join(a2)
        a33 = ''.join(a3)
        print(a11,a22,a33)
