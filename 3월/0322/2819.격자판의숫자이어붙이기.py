'''
def check(idx,r,c,num):
    num += arr[r][c]
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    if idx == 6:
        result.append(num)
        return num

    # 6번의 이동
    for i in range(4):
        # 범위 내에 있어야 함
        if 0<=r+dr[i]<4 and 0<=c+dc[i]<4:
            check(idx+1,r+dr[i],c+dc[i],num)
# 테스트 케이스의 수
T = int(input())
for tc in range(1,T+1):
    # 4*4 격자판
    arr = [list(map(str,input().split())) for _ in range(4)]

    result = []
    for r in range(4):
        for c in range(4):
            check(0,r,c,'')
    # 서로 다른 일곱자리 수들의 개수 구하기
    result_set = set(result)
    n = len(result_set)
    print(f'#{tc} {n}')
'''

# 유라
# n : idx
def DFS(n,ci,cj,num):
    if n ==7:
        sset.add(num)
        return
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj = ci+di,cj+dj
        if 0<=ni<4 and 0<=nj<4:
            DFS(n+1,ni,nj,num*10+arr[ni][nj])

# 테스트 케이스의 수
T = int(input())
for tc in range(1,T+1):
    # 4*4 격자판
    arr = [list(map(int,input().split())) for _ in range(4)]
    sset = set()
    for i in range(4):
        for j in range(4):
            DFS(0,i,j,0)
    print(f'#{tc} {len(sset)}')
