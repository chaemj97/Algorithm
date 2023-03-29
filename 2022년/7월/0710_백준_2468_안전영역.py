

from sys import stdin
from copy import deepcopy
from collections import deque
input = stdin.readline

# NxN 영역
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

# 최고 높이
x_max = 0
for i in range(N):
    i_max = max(arr[i])
    if i_max > x_max:
        x_max = i_max

max_cnt = 0
# 비가 오지 않는 경우를 생각해서 0부터 시작
for x in range(0,x_max+1):
    arr_x = deepcopy(arr)
    # x 이하인 모든 지점 물에 잠김
    # 잠김 지점 0으로 표시
    for r in range(N):
        for c in range(N):
            if arr_x[r][c] < x:
                arr_x[r][c] = 0
    cnt = 0
    # 영역 개수 세기
    for r in range(N):
        for c in range(N):
            if arr_x[r][c] != 0:
                cnt += 1
                que = deque()
                que.append([r,c])
                arr_x[r][c] = 0
                while que:
                    cr,cc = que.popleft()
                    for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                        nr = cr + dr
                        nc = cc + dc
                        if 0 <= nr < N and 0 <= nc < N and arr_x[nr][nc] != 0:
                            arr_x[nr][nc] = 0
                            que.append([nr,nc])
    # 영역의 개수가 최대인가
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)