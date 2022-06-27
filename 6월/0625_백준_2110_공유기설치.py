
 
from sys import stdin
input = stdin.readline

# 집의 개수, 공유기의 갯
N, C = map(int,input().split())

# 집의 좌표
house = []
for i in range(N):
    h = int(input())
    house.append(h)
house.sort()

# 가장 인접한 두 공유기 사이의 거리를 가능한 크게

# 집끼리 거리
dist = []
