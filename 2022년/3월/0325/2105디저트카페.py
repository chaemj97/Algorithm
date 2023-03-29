# n : 회전 횟수, (ci,cj) : 현재 위치, v : 방문한 곳 표시, cnt : 디저트 종류 수
def DFS(n,ci,cj,v):
    # (i,j) : 출발 위치
    global i,j,ans
    # 절반을 갔을 때 가지치기
    if n == 2 and ans>=len(v)*2:
        return

    if n > 3 : # 종료조건
        return
    # 정답 갱신
    # 회전 3번, 복귀, 디저트 종류 수 최대
    if n == 3 and ci == i and cj == j and ans < len(v):
        ans = len(v)
        return
    # 직진 or 방향 바꾸기
    for k in range(n,n+2):
        ni,nj = ci + di[k], cj + dj[k]
        # 범위 내, 중복 아니면
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            DFS(k,ni,nj,v)
            v.pop()

# 4번째 방향 바꾸기 : 복귀 못하므로 실패
di,dj = (1,1,-1,-1,0),(-1,1,1,-1,0)
# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 지역의 한 변의 길이
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 방문한 디저트 종류 수
    ans = -1
    for i in range(0,N-2):
        for j in range(1,N-1):
            DFS(0,i,j,[])

    print(f'#{tc} {ans}')