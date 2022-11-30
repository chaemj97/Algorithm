for _ in range(1,11):
    # 테스트 케이스 번호, 길의 총 개수
    tc, num = map(int,input().split())
    # 순서쌍
    arr = list(map(int,input().split()))

    # 갈 수 있는 도시 찾기
    adj = [[-1]*100 for _ in range(2)]
    for i in range(num):
        # 첫번째 길이라면
        if adj[0][arr[i*2]] == -1:
            adj[0][arr[i*2]] = arr[i*2+1]
        # 두번째 길이라면
        else:
            adj[1][arr[i * 2]] = arr[i * 2 + 1]

    # 방문여부
    visited = [0]*100
    visited[0] = 1
    # 가는 경로
    stack = [0]
    # 기본값은 가는 길 존재 X
    result = 0
    while stack:
        top = stack[-1]
        # 도착?
        if top == 99:
            result = 1
            break
        for i in range(2):
            # 길이 있고, 방문한적 없는 곳이면 가자
            if adj[i][top] != -1 and not visited[adj[i][top]]:
                stack.append(adj[i][top])
                visited[adj[i][top]] = 1
                break
        # 길이 업다면 되돌아가기
        else:
            stack.pop()

    print(f'#{tc} {result}')

'''
def graph(v):
    # 방문 표시
    visited[v] = 1
    for i in G[v]:
        # 방문한 적 없으면 방문
        if not visited[i]:
            graph(i)
 
 
for _ in range(10):
    # 테스트 케이스 번호, 길의 총 개수
    tc, E = map(int, input().split())
    # 순서쌍
    arr = list(map(int, input().split()))
    
    # 방문 표시
    visited = [0] * 100
    # 갈수 있는 길 표시
    G = [[] for _ in range(100)]
    for i in range(E):
        G[arr[i*2]].append(arr[i*2+1])
        
    graph(0)
    
    print(f'#{tc} {visited[99]}')
    '''