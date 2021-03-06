
def find(man):
    # 모든 자리 돌면서 비어있는지 확인, 좋아하는 학생이 인접한 칸에 많은지 확인
    like_max = -1
    empty_max = -1
    seat = [0,0]
    for r in range(N):
        for c in range(N):
            if seats[r][c] == 0: # 비어있는 자리라면
                like_cnt = 0  # 좋아하는 학생 수
                empty_cnt = 0 # 주변에 빈자리 수
                for i in range(4): # 상좌하우 확인하기, 좋아하는 친구 있는지 확인
                    nr, nc = r+dr[i], c+dc[i]
                    if 0<= nr < N and 0<= nc < N:
                        if seats[nr][nc] == 0:
                            empty_cnt += 1
                        if seats[nr][nc] in like_man:
                            like_cnt += 1
                if like_max < like_cnt or (like_max == like_cnt and empty_max < empty_cnt):
                    like_max, empty_max = like_cnt, empty_cnt
                    seat = [r,c]
    return seat

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N**2)] # 학생 번호, 좋아하는 학생들
seats = [[0]*N for _ in range(N)] # 앉는 자리
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N**2):
    if i == 0:
        seats[1][1] = arr[i][i]  # 첫번째 학생은 무조건 1,1의 자리에 있음
    else:
        like_man = arr[i][1:]
        s = find(arr[i][0])
        seats[s[0]][s[1]] = arr[i][0]

result = 0
for r in range(N):
    for c in range(N):
        student = seats[r][c]
        like_cnt = 0
        for x in range(N**2):
            if arr[x][0] == student:
                like_lst = arr[x][1:]
                break
        for i in range(4):  # 상좌하우 확인하기, 좋아하는 친구 있는지 확인
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and seats[nr][nc] in like_lst:
                like_cnt += 1
        if like_cnt:
            result += 10 ** (like_cnt -1)
print(result)
