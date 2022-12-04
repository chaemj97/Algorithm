
def check(start):
    # 시작점 초기화
    dist[start] = 0
    # N번 반복
    for i in range(1,N+1):
        # 모든 간선을 확인
        for s in range(1,N+1):
            # s에서 다음으로 이동
            for next, time in world[s]:
                # 이 간선을 거치는게 더 시간이 짧은가
                if dist[next] > dist[s] + time:
                    dist[next] = dist[s] + time
                    # N번째에서도 값이 갱신된다는 건 음수 순환이 존재
                    # == 처음으로 되돌아갈 때 시간이 거꾸로 갈 수 있음
                    if i == N:
                        return True
    return False

# 테스트케이스의 개수
TC = int(input())
for tc in range(TC):
    # 지점의 수, 도로의 개수, 웜홀의 개수
    N, M, W = map(int,input().split())
    # 두 지점을 연결하는 도로가 한 개보다 많을 수도 있다.
    world = [[] for _ in range(N+1)]
    # 도로의 정보 : 방향이 없음
    for _ in range(M):
        s,e,t = map(int,input().split())
        world[s].append([e,t])
        world[e].append([s,t])
    # 웜홀의 정보 : 방향이 있음 + 시간이 거꾸로 감
    for __ in range(W):
        s,e,t = map(int,input().split())
        world[s].append([e,-t])

    # 거리
    dist = [10001 for __ in range(N+1)]
    # 처음으로 되돌아왔을때 시간이 되돌아가 있는가?
    if check(1):
        print('YES')
    else:
        print('NO')

    
