# 입력 받는 2차원 평면의 정보를 그래프로 변환
# 헌터는 몬스터 퇴치 후, 해당 몬스터와 매칭되는 클라이언트를 방문할 수 있도록 탐색
# 클라이언트, 몬스터 모든 상호간의 맨해튼 거리를 구해 저장
# 저장된 그래프의 간선 가중치(맨해튼 거리)를 DFS로 탐색
# 탐색 시 방문 배열을 이용해 불필요한 탐색 및 중복을 줄인다
# 백트래킹을 활용하여 최단거리 이상 탐색X

# 첫 몬스터 잡은 이후 이동
# n : 재귀 횟수, location : 현재 위치(몬스터 1이면 1, 클라이언트 1이면 -1), dist : 현재까지 이동 거리 
def my_hunt(n,location,dist):
    global result, cnt
    # 다 잡고 고객방문했는가?
    if n == cnt:
        # 최소 이동거리인가?
        if result > dist:
            result = dist
        return

    # 현재 이동거리가 지금까지 최소 이동거리보다 크다면 return
    if dist > result:
        return

    # 이동해보자
    for i in range(1,cnt+1):
        if used[i]:
            continue

        # 몬스터 잡기 or 잡고 난 후 고객 방문
        used[i] = 1
        # 현재 i가 몬스터라면 클라이언트에 방문할 수 있도록 used 배열 0으로 초기화
        if i <= cnt // 2:
            used[i*(-1)] = 0
        my_hunt(n+1,i,dist+myGraph[location][i])
        # 되돌리기
        if i <= cnt // 2:
            used[i*(-1)] = 1
        used[i] = 0
    return


# 테스트 개수
T = int(input())

for tc in range(1,T+1):
    # 맵의 한변의 길이
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    
    result = float('inf')

    # cnt는 몬스터 + 클라이언트 수 저장
    cnt = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                cnt += 1

    # 맨해튼 거리 구하기 위한 좌표 저장
    # 각 포인트는 MAP에 저장된 값을 index로 가지는 위치에 좌표 (X,Y) 값이 저장
    # 몬스터의 index는 양수임으로 리스트의 앞쪽, 이와 대칭되는 클라이언트는 음수이므로 리스트의 뒤쪽부터 저장되며 각각이 매칭
    # 0에는 사냥꾼의 위치 [0,0]이 저장

    # points는 좌표 저장
    points = [[-1,-1] for _ in range(cnt+1)]
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                points[MAP[r][c]][0] = r
                points[MAP[r][c]][1] = c
    
    # 각 몬스터와 클라이언트 간의 맨해튼 거리를 저장할 배열
    myGraph = [[0 for _ in range(cnt+1)] for _ in range(cnt+1)]

    # 각 몬스터와 클라이언트 간의 맨해튼 거리 저장
    for i in range(1,cnt):
        for j in range(i+1,cnt+1):
            myGraph[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            myGraph[j][i] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    
    # 방문 배열 used
    # 0은 쓰지않는 1로 채움
    # cnt//2 기준 앞은 몬스터, 뒤는 클라이언트
    # 초기 상태는 클라이언트는 방문하지 않아야함(몬스터를 잡지 않았기 때문에)
    # 따라서 몬스터는 0, 클라이언트는 1로 초기화해주면 이를 이용해 몬스터에 먼저 방문하고 클라이언트에 방문할 수 있도록 처리
    used = [1] + [0] * (cnt//2) + [1] * (cnt//2) 

    # 처음 사냥꾼이 사냥을 할때는 몬스터만 방문함 따라서 반복문의 범위는 1~cnt//2+1
    for i in range(1,cnt//2+1):
        # 사냥꾼이 몬스터를 잡으러 가는 맨해튼 거리는 따로 구해줌
        res = points[i][0] + points[i][1]
        # 몬스터를 잡으면 몬스터는 1, 고객은 0으로 변경
        used[i*(-1)] = 0
        used[i] = 1
        # 이동!!!
        my_hunt(1,i,res)
        # 되돌리기
        used[i] = 0
        used[i*(-1)] = 1

    print(f'#{tc} {result}')