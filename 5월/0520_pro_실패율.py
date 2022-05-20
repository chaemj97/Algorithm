def solution(N, stages):
    p = [[0,0] for _ in range(N+1)]
    p[0][1] = len(stages)
    
    for i in range(1,N+1):
        # 도달했으나 아직 클리어하지 못한 플레이어 수
        p[i-1][0] = stages.count(i)
        # 도달한 사람
        p[i][1] = p[i-1][1]-p[i-1][0]
        # 실패율
        # 그 스테이지에 도달한 사람이 없는 경우 생각!!
        if p[i-1][1]:
            p[i-1][0] /= p[i-1][1]
        else:
            p[i-1][0] = 0
        # i번 스테이지
        p[i-1][1] = i
    # 실패율이 높은 순으로 
    p.sort(reverse=True, key=lambda x:x[0])
    
    answer = [p[i][1] for i in range(N)]
    return answer