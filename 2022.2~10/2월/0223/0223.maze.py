mazeArray = [
    [0,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,3]]

N = 8
# DFS = 현 상태에서 가능한 모든 경우의 수 고려하기
# 시작점
r,c = 0,0

# 현재위치 (r,c) >>> 현재 위치에서 갈 수 있는 경우의 수 모두 찾아보기
stack = []
stack.append((r,c))
# 방문했던 위치는 재방문하지 않기 위해 visited 배열 사용
visited = [[0] * N for _ in range(N)]
# 시작점 방문 표시
visited[r][c] = 1
# 4 방향을 탐색을 위해서, 변화량 배열 선언
dr = [-1,1,0,0]
dc = [0,0,-1,1]
# 상하좌우

# 1. 현재 위치 (top)에서 갈 수 있는 경로 탐색
# 2. 경로를 찾았으면, stack에 push, 방문표시하고, 즉시이동(break)
# 3. 경로가 없으면 stack.pop()
# stack이 빌 때 까지 반복
while stack:
    # 현재위치
    cr,cc = stack[-1]
    if mazeArray[cr][cc] == 3:
        print('길이 있네요')
        break
    # 현재 위치에서 갈 수 있는 길 찾기
    for d in range(4):
        nr = cr + dr[d]
        nc = cc + dc[d]
        # 갈 수 없는 길이면 안가면 됨
        # 갈 수 없는 길 : 범위를 벗어나거나, 벽, 방문했거나
        if 0 <= nr < N and 0 <= nc < N and mazeArray[nr][nc] != 1 and not visited[nr][nc]:
            # 스택추가
            stack.append((nr,nc))
            # 방문표시
            visited[nr][nc] = 1
            break
    # 네 방향을 다 살펴봤는데 break가 한번도 안걸림 -> 갈 수 있는 길 없다
    else:
        stack.pop()