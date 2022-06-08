def solution(N, road, K):
    # 마을 간 걸리는 시간 2차원 행렬로 정리 
    path = [[0]*(N+1) for _ in range(N+1)]
    for r in road:
        # 아직 도로가 없다면 추가
        if path[r[0]][r[1]] == 0:
            path[r[0]][r[1]] = r[2]
            path[r[1]][r[0]] = r[2]
        # 도로가 있다면 걸리는 시간이 더 적은 도로를 남기기
        else:
            path[r[0]][r[1]] = min(path[r[0]][r[1]],r[2])
            path[r[1]][r[0]] = path[r[0]][r[1]]

    # 걸리는 시간
    time = [0]*(N+1)
    # 1번 마을은 항상 가능하니 숫자 10
    time[1] = 10
    q = [1]
    while q:
        now = q.pop(0)
        for idx,i in enumerate(path[now]):
            # 도로가 있고 K시간 이하 배달 가능이면 (1번 마을 도착을 10으로 둬서 K아니고 K+10으로 계산하기)
            if i and time[now] + i <= K+10:
                # 이미 도착한 적이 있다면 이전 방법과 지금 방법의 시간 비교 -> 더 적게 걸린 시간 남기기
                if time[idx]:
                    if time[now]+i < time[idx]:
                        time[idx] = time[now] + i
                        q.append(idx)
                # 도착한 적 없으면 
                else:
                    time[idx] = time[now] + i
                    q.append(idx)  
    # 도착한 시간이 적힌 마을 세기(도착한 시간이 0이면 도착 못 한 마을)
    return N+1-time.count(0)