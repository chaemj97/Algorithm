# https://chaemi720.tistory.com/179

from sys import stdin

input = stdin.readline
# 사람의 수
N = int(input())
# 각 사람이 돈을 인출하는데 걸리는 시간
P = list(map(int,input().split()))

P.sort()

time = 0
for idx,pi in enumerate(P):
    time += pi * (N - idx)

print(time)