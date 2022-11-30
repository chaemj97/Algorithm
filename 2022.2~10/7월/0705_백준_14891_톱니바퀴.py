

from sys import stdin
from collections import deque
input = stdin.readline

# 톱니바퀴의 상태 (12시 방향부터)
# N극은 0, S극은 1
# 맞닿는 idx : 2,6
sawtooth = [0] + [deque(list(map(int,list(input().rstrip())))) for _ in range(4)]

# 톱니바퀴 오른쪽 확인
# 현재꺼의 6번과 원래꺼의 2번 비교
def check_right(idx,d):
    # 오른쪽에 확인 할 게 없거나 같은 극이라서 회전하지 않는다면
    if idx > 4 or sawtooth[idx-1][2] == sawtooth[idx][6]:
        return
    if sawtooth[idx-1][2] != sawtooth[idx][6]:
        # 다음 톱니가 회전 가능한지 확인
        check_right(idx+1,-d)
        # 회전
        sawtooth[idx].rotate(d)
    

# 톱니바퀴 왼쪽 확인
# 현재꺼의 2번과 원래꺼의 6번 비교
def check_left(idx,d):
    # 오른쪽에 확인 할 게 없거나 같은 극이라서 회전하지 않는다면
    if idx < 1 or sawtooth[idx][2] == sawtooth[idx+1][6]:
        return
    if sawtooth[idx][2] != sawtooth[idx+1][6]:
        # 다음 톱니가 회전 가능한지 확인
        check_left(idx-1,-d)
        # 회전
        sawtooth[idx].rotate(d)


# 회전 횟수
K = int(input())
# 1: 시계 방향, -1 : 반시계 방향
# 회전
for _ in range(K):
    # 회전시킨 톱니바퀴 번호, 방향
    num,d = map(int,input().split())
    # 오른쪽 확인
    check_right(num+1,-d)
    # 왼쪽 확인
    check_left(num-1,-d)
    # 다 확인 후 자기 자신 돌리기
    sawtooth[num].rotate(d)

# 점수계산
score = 0
for i in range(1,5):
    # i번 톱니바퀴의 12시방향이 S극이면
    if sawtooth[i][0] == 1:
        score += 2**(i-1)
print(score)
        