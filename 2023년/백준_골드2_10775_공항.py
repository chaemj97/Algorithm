'''
    접근법 1
        도킹했다면 그 자리 도킹 못하니 그 앞 칸에 연결해두기
        그래서 다음번에 그 번호에 도킹하려고할 때 앞 칸으로 이동

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 게이트의 수
G = int(input())
gate = [i for i in range(G+1)]
# 비행기의 수
P = int(input())
plane = [int(input()) for _ in range(P)]

def parent(p):
    if p != gate[p]:
        gate[p] = parent(gate[p])
    return gate[p]

answer = 0
for p in plane:
    x = parent(p)
    # 0과 연결되었다면 빈 자리 없음
    if x == 0:
        break
    # 한 칸 채우기
    gate[x] -= 1
    answer += 1

print(answer)