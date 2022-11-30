def DFS(n,ssum):
    global ans
    if n > 12:
        if ans > ssum:
            ans = ssum
        return
    # 1일
    DFS(n+1, ssum + month[n]*day)
    # 1달
    DFS(n + 1, ssum + mon)
    # 3달
    DFS(n + 3, ssum + mon3)
    # 1년
    DFS(n + 12, ssum + year)
# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 이용권 가격들 (1일,1달,3달,1년)
    day, mon, mon3, year = map(int,input().split())
    # 12개월 이용 계획
    month = [0]+list(map(int,input().split()))
    ans = 1000000000000
    DFS(1,0)
    print(f'#{tc} {ans}')

'''
T = int(input())
for tc in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    month = [0]+list(map(int, input().split()))
    D = [0]*13
    for i in range(1, 13):
        mmin = D[i-1] + month[i]*day
        mmin = min(mmin, D[i-1] + mon)
        if i>=3:
            mmin = min(mmin, D[i - 3] + mon3)
        if i>=12:
            mmin = min(mmin, D[i - 12] + year)
        D[i]=mmin
    print(f'#{tc} {D[12]}')
'''
