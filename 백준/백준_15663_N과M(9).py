from sys import stdin
input = stdin.readline

# N개의 자연수 중에서 M개 고르기
N, M = map(int,input().split())
num = sorted(map(int,input().split()))
# 골랐는가?
used = [0]*N
tmp = []

def check(i):
    # M개 골랐는가?
    if i == M:
        print(*tmp)
        return

    # 이번 고른거에 중복된 수를 확인 할 필요 없
    dup = 0

    # 고르기
    for j in range(N):
        # 사용했는가? 이번 고르기에 골랐던 수인가?
        if used[j] == 0 and dup != num[j]:
            # 사용 표시
            used[j] = 1
            tmp.append(num[j])
            dup = num[j]
            check(i+1)
            # 되돌리기
            used[j] = 0
            tmp.pop()

check(0)