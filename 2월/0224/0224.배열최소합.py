import sys
sys.stdin = open('sample_input.배열.txt')

# N : 행의 수, arr : N*N 배열, idx : 행의 인덱스, sum : 각 행의 1개씩 합
def sum_min(N,arr,idx,sum):
    if idx == N:
        return sum
    min_result = 1000000000
    for i in range(N):
        # 방문하지 않은 열이면 가능
        if visited[i] == 0:
            visited[i] = 1
            result = sum_min(N,arr,idx+1,sum + arr[idx][i])
            if result < min_result:
                min_result = result
            visited[i] -= 1
    return min_result
# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N*N 배열
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N

    min_v = sum_min(N,arr,0,0)

    print(f'#{tc} {min_v}')









