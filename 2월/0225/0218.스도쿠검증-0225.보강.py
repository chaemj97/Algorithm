import sys
sys.stdin = open('./input.스도쿠.txt')

# 스도쿠를 만족하면 1을 return, 아니면 0을 return
def check():
    # 가로
    for r in range(9):
        cnt = [0] * 10
        for c in range(9):
            t = ARR[r][c]
            if cnt[t] == 1:
                return 0
            cnt[t] = 1
    # 세로
    for c in range(9):
        cnt = [0] * 10
        for r in range(9):
            t = ARR[r][c]
            if cnt[t] == 1:
                return 0
            cnt[t] = 1

    for stR in range(0,9,3):
        for stC in range(0,9,3):
            cnt = [0]*10
            for r in range(3):
                for c in range(3):
                    t = ARR[stR + r][stC + c]
                    if cnt[t] == 1:
                        return 0
                    cnt[t] = 1

    return 1


# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    ARR = [list(map(int,input().split())) for _ in range(9)]



    result = checkarr)
    print(f'#{tc} {result}')