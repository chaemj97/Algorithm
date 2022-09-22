from itertools import combinations

# 0: 빈칸, 1: 집, 2: 치킨집

# 도시 크기 N*N, 남을 치킨집에 개수 M
N,M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]

# 집/치킨집 위치 구하기
home = []
chicken = []
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            home.append((r,c))
        elif city[r][c] == 2:
            chicken.append((r,c))

# 도시의 치킨 거리 최솟값
answer = float('inf')

# 치킨집 M개 순열로 뽑기
for ls in combinations(chicken,M):
    # 도시의 치킨 거리
    dist = 0
    # 각 집의 치킨 거리 구하기
    for i in home:
        dd = float('inf')
        for j in ls:
            dd = min(dd,abs(i[0]-j[0]) + abs(i[1]-j[1]))
        dist += dd
    # 최소 거리
    answer = min(answer,dist)

print(answer)

