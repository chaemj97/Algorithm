'''
    접근법
    
'''
import heapq
import sys
input = sys.stdin.readline

# 테스트 케이스 수
T = int(input())
for t in range(1,T+1):
    # 관계의 수, 정치인의 수
    n,m = map(int,input().split())
    # 관계 표시
    f = [[] for _ in range(m)]
    for _ in range(n):
        # 정치인, 그의 친구, 친밀도
        x,y,z = map(int,input().split())
        f[x].append([z,y])
        f[y].append([z,x])
    
    
    