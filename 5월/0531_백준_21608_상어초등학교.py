# https://chaemi720.tistory.com/139

# 교실 크기 N*N
N = int(input())

# 좋아하는 학생 리스트
# idx(0)은 idx(1~4) 좋아해
like = [list(map(int,input().split())) for _ in range(N**2)]

# 교실
seat = [[0]*N for _ in range(N)]

# 나의 자리는?
for me in range(N**2):
    # 내가 앉을 자리
    me_r,me_c = 0,0
    # 인접한 자리에 좋아하는 학생 수, 비어 있는 자리 수
    me_likepeoplecnt, me_emptycnt = -1,-1

    # 모두 돌아보자
    for r in range(N):
        for c in range(N):
            # 빈자리인지부터 확인
            if not seat[r][c]:
                # r,c의 인접한 자리에 좋아하는 학생 수
                likepeoplecnt = 0
                # r,c의 인접 빈 자리
                emptycnt = 0
                # 인접 자리 확인 해보자
                for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr = r + dr
                    nc = c + dc
                    # 교실 내의 자리
                    if 0 <= nr < N and 0 <= nc < N:
                        # 이 자리에 내가 좋아하는 사람이 앉았나?
                        if seat[nr][nc] in like[me]:
                            likepeoplecnt += 1
                        # 빈자리?
                        if seat[nr][nc] == 0:
                            emptycnt += 1

                # 현 위치가 최상의 자리인가?
                # 최상의 자리 :인접자리에 좋아하는 사람수가 가장 많으면서 인접에 빈자리가 많음
                if likepeoplecnt > me_likepeoplecnt or (likepeoplecnt == me_likepeoplecnt and emptycnt > me_emptycnt):
                    # 갱신
                    me_r,me_c = r,c
                    me_likepeoplecnt, me_emptycnt = likepeoplecnt, emptycnt
    # 내자리 앉기
    seat[me_r][me_c] = like[me][0]


# 다 앉았으면 만족도 조사
good = 0
for r in range(N):
    for c in range(N):
        # 나의 만족도
        likecnt = 0
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr = r + dr
            nc = c + dc
            # 교실 내의 자리
            if 0 <= nr < N and 0 <= nc < N:
            # 이 자리에 내가 좋아하는 사람이 앉았나?
                if seat[nr][nc] in [x for x in like if x[0]==seat[r][c]][0]: # 여기가 문제!!!
                    # in 다음 자리에 seat[r][c] 번 사람의 좋아하는 사람 리스트를 넣고 싶음...
                    # [x for x in like if x[0]==seat[n][r]]
                    likecnt += 1
        # 만족도 점수 더하기 (10의 거듭제곱)
        if likecnt:
            good += 10**(likecnt-1)

print(good)