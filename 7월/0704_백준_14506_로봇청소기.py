

from sys import stdin
input = stdin.readline
# 장소 세로, 가로
N, M = map(int,input().split())
# [r,c,d]
robotClean = [list(map(int,input().split()))]
# d : 북,동,남,서
# 왼쪽 : d[(idx-1)%4]
# 뒤쪽 : d[(idx-2)%4]
d = [[-1,0],[0,1],[1,0],[0,-1]]

# 장소의 상태 : 0은 빈칸, 1은 벽
place = [list(map(int,input().split())) for _ in range(N)]

# 회전만 한 횟수
onlyRotateCnt = 0
# 청소하기
while True:
    # 현재 위치
    cr,cc,cd = robotClean[-1]
    # 회전만 4번 했을 때
    if onlyRotateCnt == 4:
        # 뒤쪽이 벽이면 멈추기
        back_r = cr + d[(cd-2)%4][0]
        back_c = cc + d[(cd-2)%4][1]
        if place[back_r][back_c] != 0:
            break
        # 뒤쪽이 벽이 아니면 멈추기
        else:
            robotClean.append([back_r,back_c,cd])
    # 청소하기
    else:
        # 현재 위치 청소
        place[cr][cc] = 1
        # 왼쪽 위치
        left_d = (cd-1)%4
        left_r = cr + d[left_d][0]
        left_c = cc + d[left_d][1]
        # 왼쪽에 청소하지 않은 빈 공간이 존재한다면 이동
        if 0 <= left_r < N and 0 <= left_c < M and place[left_r][left_c] == 0:
            robotClean.append([left_r,left_c,left_d])
            onlyRotateCnt = 0
        # 왼쪽에 청소하지 않은 빈 공간이 없다면 방향만 회전
        else:
            robotClean[-1][2] = left_d
            onlyRotateCnt += 1

print(robotClean,len(robotClean))