# https://chaemi720.tistory.com/138

# # 미로 크기 N*M
# # 1이동, 0이동X
# # (1,1)출발 -> (N,M) 도착 : 이동 중 지나야 하는 최소의 칸 수 구하기
# # 칸 셀 때 시작과 도착 포함

# # 미로 
# N,M = map(int,input().split())
# maze = [list(map(int,input())) for _ in range(N)]

# # 최소이동거리 찾는 거니깐 큐
# # (행, 열, 이동한 칸 수)
# # 이동한 칸 수(시작 위치 포함이므로 1부터 시작)
# que = [(0,0,1)]

# # 방문한 곳 표시
# visited = [[0]* M for _ in range(N)]
# visited[0][0] = 1

# while que:
#     # 현 위치
#     cr,cc,cnt = que.pop(0)
#     # 도착
#     if cr == N-1 and cc == M-1:
#         # 무조건 도착
#         print(cnt)
#         break
#     # 4방향 이동해보자 ( 오른쪽,아래쪽,왼쪽,위쪽)
#     for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
#         nr = dr + cr
#         nc = dc + cc
#         # 미로 안, 이동할 수 있는(벽(0)이 아니고, 방문 한 적 없어야 함) 
#         if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] and not visited[nr][nc]:
#             que.append((nr,nc,cnt+1))
#             # 방문 표시
#             visited[nr][nc] = 1
        
# deque
from collections import deque
# 미로
N,M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]

deq = deque()
# 시작점
deq.append((0,0))

while deq:
    # 현재 위치
    cr,cc = deq.popleft()
    # 도착?
    if cr == N-1 and cc == M-1:
        print(maze[N-1][M-1])
        break
    # 4방향 이동해보자 ( 오른쪽,아래쪽,왼쪽,위쪽)
    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr = dr + cr
        nc = dc + cc
        # 미로 안, 이동할 수 있는(벽(0)이 아니고 방문한 적 없음) 
        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
            deq.append((nr,nc))
            # 이전 위치에서 1칸 이동, 미로 위에 직접 출발지로부터 거리 입력
            maze[nr][nc] = maze[cr][cc] + 1
            