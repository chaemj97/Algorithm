import sys
sys.stdin = open('input.길찾기.txt')

# 테스트 케이스의 개수
T = 10
for _ in range(T):
    # 테스트 케이스의 번호, 길의 총 개수
    tc, N = map(int, input().split())
    # 순서쌍
    arr = list(map(int,input().split()))
    # 인접 : 한개의 정점에서 선택할 수 있는 길 최대 2개
    # 정점 번호에 0이 있기 때문에 -1로 설정
    adj = [[-1]*100 for _ in range(2)]

    for i in range(0,N*2,2):
        # (1,2)라면 1에서 2로 가는 길
        # adj[0][1]에 2 대입
        # 처음 길
        if adj[0][arr[i]] == -1:
            adj[0][arr[i]] = arr[i+1]
        # 두번째 길
        else:
            adj[1][arr[i]] = arr[i+1]
    # 0에서 99로 가는길이 있으면 1, 없으면 0
    result = 0

    stack = []
    stack.append(0)
    visited = [0]*100
    visited[0] = 1

    while stack:
        top = stack[-1]
        # 99에 도착?
        if top == 99:
            result = 1
            break
        # top와 인접하고 방문한 적 없으면 방문하기
        if adj[0][top] and not visited[adj[0][top]]:
            stack.append(adj[0][top])
            visited[adj[0][top]] = 1

        elif adj[1][top] and not visited[adj[1][top]]:
            stack.append(adj[1][top])
            visited[adj[1][top]] = 1

        # 경로가 없다면 되돌아가기
        else:
            stack.pop()
    print(f'#{tc} {result}')

    # 교수님
    # while stack:
    #     top = stack[-1]
    #     # 99에 도착?
    #     if top == 99:
    #         result = 1
    #         break
    #     for i in range(2):
    #         # top와 인접하고 방문한 적 없으면 방문하기
    #         if adj[i][top] != -1 and not visited[adj[i][top]]:
    #             stack.append(adj[i][top])
    #             visited[adj[i][top]] = 1
    #             break
    #     # 경로가 없다면 되돌아가기
    #     else:
    #         stack.pop()
