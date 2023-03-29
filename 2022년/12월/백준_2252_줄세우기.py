from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int,input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    # a가 b보다 먼저
    a,b = map(int,input().split())
    graph[a].append(b)
    # 진입 차수 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result = []
    # 큐 기능을 위한 deque
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for j in graph[now]:
            indegree[j] -= 1
            # 새롭게 진입 차수가 0이 되는 노드는 큐에 삽입
            if indegree[j] == 0:
                q.append(j)
    # 위상 정렬을 수행한 결과 출력
    print(*result)

topology_sort()