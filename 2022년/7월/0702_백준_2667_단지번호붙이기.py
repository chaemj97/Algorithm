

# from sys import stdin
# input = stdin.readline

# --------------------------------------------
# 스택

# # 지도의 크기
# N = int(input())
# arr = [list(map(int,input().rstrip())) for _ in range(N)]

# def dfs(r,c):
#     stack = [(r,c)]
#     arr[r][c] = 0
#     # 이번 단지내 집의 수
#     cnt = 1
#     while stack:
#         cr,cc = stack[-1]
#         # 4방향으로 움직여보자
#         for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
#             nr = cr + dr
#             nc = cc + dc
#             # 지도 내에 있고 단지에 등록되지 않은 건물이라면
#             if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
#                 cnt += 1
#                 arr[nr][nc] = 0
#                 stack.append((nr,nc))
#                 break
#         else:
#             stack.pop()
#     return cnt

# # 단지 번호
# dangi_num = 0
# # 각 단지내 집의 수
# dangi_list = []
# for r in range(N):
#     for c in range(N):
#         # 집이 있고 아직 단지로 묶지 않았다면
#         if arr[r][c] == 1:
#             dangi_num += 1
#             # 이번 단지 단지내 집의 수 구하기
#             dangi_cnt = dfs(r,c)
#             dangi_list.append(dangi_cnt)

# # 각 단지내 집의 수 오름차순으로 정렬
# dangi_list.sort()

# print(dangi_num)
# for c in dangi_list:
#     print(c)

# --------------------------------------------
# 큐

from sys import stdin
from collections import deque
input = stdin.readline

# 지도의 크기 
N = int(input())
arr = [list(map(int,input().rstrip())) for _ in range(N)]

def bfs(r,c):
    que = deque()
    que.append((r,c))
    arr[r][c] = 0
    # 이번 단지내 집의 수
    cnt = 1
    while que:
        cr,cc = que.popleft()
        # 4방향으로 확인
        for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
            nr = cr + dr
            nc = cc + dc
            # 지도 내에 있고 단지에 등록되지 않은 건물이라면
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                cnt += 1
                arr[nr][nc] = 0
                que.append((nr,nc))
    return cnt

# 단지 번호
dangi_num = 0
# 각 단지내 집의 수
dangi_list = []
for r in range(N):
    for c in range(N):
        # 집이 있고 아직 단지로 묶지 않았다면
        if arr[r][c] == 1:
            dangi_num += 1
            # 이번 단지 단지내 집의 수 구하기
            dangi_cnt = bfs(r,c)
            dangi_list.append(dangi_cnt)

# 각 단지내 집의 수 오름차순으로 정렬
dangi_list.sort()

print(dangi_num)
for c in dangi_list:
    print(c)