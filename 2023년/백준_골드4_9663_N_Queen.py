'''
    접근법 1
        N-Queen
            퀸의 일직선 및 대각선 상에는 아무것도 놓이면 안된다.

        놓은 위치 저장을 2차원 배열이 아닌 1차원 리스트로 저장 (메모리 효율을 위해)
'''

import sys
input = sys.stdin.readline

N = int(input())
# 각 열마다 행번호(중복 없어야 함)
row = [0]*N
answer = 0

# x행에 놓는거 가능한가?
def check(x):
    for j in range(x):
        # 이전에 사용한 열 X / 이전에 놓은 것의 대각선 위치 X
        if row[x] == row[j] or abs(row[x] - row[j]) == x - j:
            return False
    return True

def n_queen(x):
    global answer
    # 다 놓았는가?
    if x == N:
        answer += 1
        return
    # n-queen 놓기
    # i : 행 번호
    for i in range(N):
        # x번째 열에 i번째 행 고르기
        row[x] = i
        # (x,i)에 놓는거 가능?
        if check(x):
            # 가능 하면 다음 행으로 이동
            n_queen(x+1)

n_queen(0)
print(answer)