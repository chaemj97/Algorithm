# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력
# 시작은 1
# 입력 1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7
# 결과 -1-2-4-6-5-7-3

data = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
N = max(data)
# 인접
adj = [[0]*(N+1) for _ in range(N+1)]
# 인접 표시
for i in range(0,len(data),2):
    r,c = data[i],data[i+1]
    adj[r][c] = 1
    adj[c][r] = 1

# DFS 시작
# 1. 노드 방문
#   1-1. 방문했는가? 방문했으면 방문하지 않기
#   1-2. 안했으면, 노드번호를 stack에 넣기
# 2. 현재 노드(stack의 top)에서 갈 수 있는 경로 탐색
#   2-1. 경로 발견 -> 경로로 이동
#   2-2. 발견 못하면 -> 이전 경로로 되돌아가기(pop)
# 1~2 반복 (stack이 빌 때까지)

stack = []
# 방문 표시
visited = [0]*(N+1)
# 시작 정점은 1
start = 1
stack.append(start)
visited[start] = 1
# 이동 경로
path = []
path.append(start)

# stack이 빌 때까지 반복
while stack:
    # 현재 위치
    top = stack[-1]
    # 현재 위치에서 갈 수 있는 경로 탐색 : 인접행렬
    for i in range(1,N+1):
        # 현재위치와 인접하고 방문한 적 없다면
        if adj[top][i] == 1 and not visited[i]:
            # 방문
            stack.append(i)
            visited[i] = 1
            path.append(i)
            break
    # 갈 수 있는 길이 없다면 이전 경로로 되돌아가기
    else:
        stack.pop()
for i in path:
    print('-',end='')
    print(i,end='')