from sys import stdin
from collections import deque
input = stdin.readline

# 전위 순회, 중위 순회, 후위 순회 결과 출력

# 노드의 개수
N = int(input())

# 연결 노드
node = [[] for _ in range(N+1)]
# 부모 노드 번호
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

que = deque()
que.append(1)
while que:
    n = que.popleft()
    # n번 노드랑 연결된 노드들
    for i in node[n]:
        # 부모가 정해지지 않았다면 n이 부모
        if parent[i] == 0:
            parent[i] = n
            que.append(i)

# 부모 노드 번호 출력
for j in parent[2:]:
    print(j)