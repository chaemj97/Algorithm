# https://chaemi720.tistory.com/140

# 전체 사람의 수
n = int(input())
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
a,b = map(int,input().split())

# 부모 자식간의 관계의 개수 m
m = int(input())
# 부모 자식간의 관계
relations = [list(map(int,input().split())) for _ in range(m)]

# a와 b의 거리 계산이라 que -> deque
from collections import deque

deq = deque()
# (나,아빠) -> (아빠, 할아버지) -> (할아버지,작은아빠),(할아버지,큰아빠)
deq.append((0,a))

# 촌 수 표시
chon = [0]*(n+1)
# 가장 가까운 촌 수로 확인하기 위해 스스로 1촌 표시(마지막 계산에서 1 빼기)
chon[a] = 1

# 촌 수 구하기
while deq:
    aa,bb = deq.popleft()
    # b와의 촌 수를 구함
    if b in [aa,bb]:
        break
    # 촌 수 구하기
    for r in range(m):
        for c in range(2):
            if relations[r][c] == bb:
                # 촌수를 계산한 적 없다면 추가 + 촌수 계산
                if c == 0 and chon[relations[r][1]] == 0:
                    deq.append((bb, relations[r][1]))
                    chon[relations[r][1]] = chon[bb] + 1
                elif c ==1 and chon[relations[r][0]] == 0:
                    deq.append((bb, relations[r][0]))
                    chon[relations[r][0]] = chon[bb] + 1
                break
print(chon[b]-1)