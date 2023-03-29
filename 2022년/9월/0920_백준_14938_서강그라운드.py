from stringprep import c22_specials
import sys
INF = sys.maxsize
# 지역의 개수, 수색범위, 길의 개수
n,m,r = map(int,input().split())

# 각 구역의 아이템 수
t = list(map(int,input().split()))

# 필드
arr = [[INF]*n for _ in range(n)]

# 자기 자신으로 가는 경로 거리는 0
for i in range(n):
    arr[i][i] = 0

# 길의 양 끝에 존재하는 지역의 번호 a,b / 길의 길이 l
for _ in range(r):
    a,b,l = map(int,input().split())
    arr[a-1][b-1] = l
    arr[b-1][a-1] = l

# 각 지역으로 가는 최소거리 구하기
for b in range(n):
    for a in range(n):
        for c in range(n):
            # a에서 c로 갈때 b를 거쳐갈까?
            # print(a,b,c,arr[a][c])
            if arr[a][c] > arr[a][b] + arr[b][c]:
                arr[a][c] = arr[a][b] + arr[b][c]

# 필드에서 얻을 수 있는 아이템 최대 개수
answer = 0


# 각 지역마다 최소거리로 이동할 수 있는 지역의 아이템 수 합하기
for i in range(n):
    item = 0
    visited = [0]*n
    for j in range(n):
        # 수색범위 내인가?
        if arr[i][j] <= m:
            visited[j] = 1
            item += t[j]
    # 최대 아이템인가?
    answer = max(answer,item)

print(answer)
