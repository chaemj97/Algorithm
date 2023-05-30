'''
    접근법
        플로이드 워셜
    
'''

import sys
input = sys.stdin.readline

# 물건의 개수
n = int(input())
# 물건 쌍의 개수
m = int(input())
thing = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    # a > b
    a,b = map(int, input().split())
    thing[a][b] = 1

for i in range(1,n+1):
    thing[i][i] = 1


# i -> j -> k
for j in range(1,n+1):
    for i in range(1,n+1):
        for k in range(1,n+1):
            # i -> j and j -> k : i -> k
            if thing[i][j] and thing[j][k]:
                thing[i][k] = 1

# 각 물건에 대해서 그 물건과의 비교 결과를 알 수 없는 물건의 개수
for r in range(1,n+1):
    answer = 0
    # r번과 비교 결과 알 수 없는 물건 수 세기
    for c in range(1,n+1):
        if thing[r][c] == 0 and thing[c][r] == 0:
            answer += 1
    print(answer)