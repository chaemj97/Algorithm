# dfs stack을 이용한 반복문 구성 가능

edges = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
# 인접행렬 만들기
V = 7
adj = [[0]*(V+1) for _ in range(V+1)]
adj_list = [[] for _ in range(V+1)]
for i in range(0,len(edges),2):
    a,b = edges[i], edges[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
    adj_list[a].append(b)
    adj_list[b].append(a)

for row in adj:
    print(row)
print('----------')
for row in adj_list:
    print(row)

def dfs():
    stack = [] # 방문한 경로를 저장할 stack
    # 노드를 방문하면, stakc에 경로를 추가
    # 해당경로에서 방문할 수 있는 노드가 없으면, stack 삭제
    # 위 작업들을 stack의 요소가 모두 삭제될 때까지 반복
    visited = [0]*(V+1)
    stack.append(1)
    visited[1] = 1
    while stack:
        top = stack.pop()
        print(top,end=' ')
        for i in range(V+1):
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
    print()
dfs()

