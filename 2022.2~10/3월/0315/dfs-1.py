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

def dfs():
    stack = [] #방문한 경로를 저장할 stack
    # 노드를 방문하면, stack에 경로를 추가
    # 해당경로에서 방문할 수 있는 노드가 없으면, stack에서 삭제
    # 위 작업들을 stack 의 요소가 모두 삭제될 때 까지 반복
    visited = [0] * (V+1)
    stack.append(1)
    visited[1] = 1
    print(1,end=' ')
    while stack:
        top = stack[-1]
        for i in range(V+1):
            if adj[top][i] and not visited[i]:
                print(i, end=' ')
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
    print()

# v : 현재 방문중인 노드의 번호
visited = [0] * (V+1)
def dfs2(v):
    # v 번노드에서 갈 수 있는 경로 모두 방문해보기
    visited[v] = 1
    print(v,end=' ')
    for k in adj_list[v]:
        if not visited[k]:
            dfs2(k)

# dfs()
print('===============')
dfs2(1)
