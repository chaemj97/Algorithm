#dfs stack을 이용한 반복문 구성 가능

edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# 인접행렬 만들기
V = 7
adj = [[0] * (V+1) for _ in range(V+1)]
adj_list = [[] for _ in range(V+1)]
for i in range(0,len(edges),2):
    a,b = edges[i], edges[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
    adj_list[a].append(b)
    adj_list[b].append(a)

# for row in adj:
#     print(row)
# print('========')
# for row in adj_list:
#     print(row)

def bfs():
    queue = [] #방문한 경로를 저장할 queue
    visited = [0] * (V+1)
    queue.append(1)
    visited[1] = 1
    while queue:
        front = queue.pop(0)
        print(front, end=' ')
        for i in range(V+1):
            if adj[front][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
    print()
bfs()
