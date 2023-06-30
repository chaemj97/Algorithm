'''
    접근법
        j번째 포인트 빼기
        j번째 포인트는 j-1번 포인트와 j+1번 포인트와 연결되어있다.
        j와 j-1 / j와 j+1 연결 끊고 j-1과 j+1 연결하기
    
'''
import sys
input = sys.stdin.readline

# 체크 포인트의 수
n = int(input())
point = [list(map(int,input().split())) for _ in range(n)]

# 모든 포인트 다 지난다고 생각
dist = []
for i in range(1,n):
    d = abs(point[i][0]-point[i-1][0])+abs(point[i][1]-point[i-1][1])
    dist.append(d)

# 모든 포인트 지나는 거리
total = sum(dist)    

answer = float('inf')

for j in range(1,n-1):
    d = total - (dist[j-1]+dist[j]) + abs(point[j-1][0]-point[j+1][0]) + abs(point[j-1][1]-point[j+1][1])
    # 최소거리?
    answer = min(answer,d)

# 결과 출력
print(answer)