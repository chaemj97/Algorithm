# person : 직원 번호, p : 성공 확률
def check(person,used,p):
    global max_p
    # 확률 이미 낮으면 버리기
    if max_p >= p:
        return
    # 일 분배 끝
    if person == N:
        if max_p < p:
            max_p = p
        return
    for i in range(N):
        # 분배된 적 없는 일
        if used[i] == 0:
            # 분배
            used[i] = 1
            check(person+1,used,p*p_arr[person][i]*0.01)
            # 되돌리기
            used[i] = 0

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N명의 직원, N개의 작업
    N = int(input())
    p_arr = [list(map(int,input().split())) for _ in range(N)]

    # 성공 최대 확률
    max_p = 0
    check(0,[0]*N,1)

    print(f'#{tc} {max_p*100:.6f}')