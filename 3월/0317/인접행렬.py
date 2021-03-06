import pprint
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# V : 정점의 개수, E : 간선의 개수
V,E = map(int,input().split())
arr = list(map(int,input().split()))
# 인접 행렬
adj = [[0]*(V+1) for _ in range(V+1)]
# 인접 리스트
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1,n2 = arr[i*2],arr[i*2+1]
    adj[n1][n2] = 1 # n1과 n2 인접
    adj[n2][n1] = 1 # 방향 표시가 없는 경우

    adjList[n1].append(n2)
    adjList[n2].append(n1)


pprint.pprint(adj)
pprint.pprint(adjList)