# https://chaemi720.tistory.com/168

import sys

# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

INF = sys.maxsize
money = [[INF]*n for _ in range(n)]

for _ in range(m):
    # [버스 시작 도시, 버스 도착 도시, 한번 타는데 필요한 비용]
    a,b,c = map(int,input().split())
    # 버스번호는 1번부터, index는 0번부터
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
    money[a-1][b-1] = min(money[a-1][b-1],c)

# 자기 자신으로 가는 경우
for i in range(n):
    money[i][i] = 0

# k : 거치는 곳, i : 시작, j : 도착
for k in range(n):
    for i in range(n):
        for j in range(n):
        	# 시작에서 도착으로 가는게 k를 거쳐가는 것보다 크면
            if money[i][j] > money[i][k] + money[k][j]:
                money[i][j] = money[i][k] + money[k][j]

# 출력
for i in range(n):
    for j in range(n):
        # i에서 j로 갈 수 없다면
        if money[i][j] == INF:
            print(0,end=' ')
        else:
            print(money[i][j],end=' ')
    print()
