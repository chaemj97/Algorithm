import sys
input = sys.stdin.readline

# 표의 크기 (N*N), 구해야 하는 횟수
N, M = map(int,input().split())

# 표
arr = [[0]*(N+1)] + [[0] + list(map(int,input().split())) for _ in range(N)]

# 시간 초과
# def cal(x1,y1,x2,y2):
#     answer = 0
#     for r in range(x1-1,x2):
#         answer += sum(arr[r][y1-1:y2])
#     return answer

def cal2(arr):
    cum_arr = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            # cum_arr[i-1][j-1] : cum_arr[i-1][j], cum_arr[i][j-1]에서 겹치는 부분
            cum_arr[i][j] = cum_arr[i-1][j] + cum_arr[i][j-1] - cum_arr[i-1][j-1] + arr[i][j]
    return cum_arr

# 누적합 구하기
cum_arr = cal2(arr)
for __ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    # 시간 초과
    # print(cal(x1,y1,x2,y2))
    result = cum_arr[x2][y2] - cum_arr[x2][y1-1] - cum_arr[x1-1][y2] + cum_arr[x1-1][y1-1]
    print(result)
    