'''
    접근법
        모든 개미가 땅으로 떨어질 때까지 가장 빠른 시간
            -> 각 개미가 땅에 떨어지는 가장 빠른 시간 중 최댓값
            
        모든 개미가 땅으로 떨어질 때까지 가장 느린 시간
            -> 제일 왼쪽 개미가 오른쪽으로 떨어지는 경우, 제일 오른쪽 개미가 왼쪽으로 떨어지는 경우 중 최대
    
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 막대의 길이, 개미의 수
    l,n = map(int,input().split())
    ant = sorted([int(input()) for _ in range(n)])
    
    # 모든 개미가 땅으로 떨어질 때까지 가장 빠른 시간
    min_time = []
    for i in range(n):
        # i번 개미가 땅에 떨어지는 가장 빠른 시간
        min_time.append(min(ant[i],l-ant[i]))
    # 모든 개미가 땅에 다 떨어지는 빠른 시간 (== 개미가 땅에 떨어지는 가장 빠른 시간 중 최대)
    min_time = max(min_time)

    # 모든 개미가 땅으로 떨어질 때까지 가장 느린 시간
    # 1. 제일 오른쪽 개미가 왼쪽으로 떨어지는 경우 : ant[-1]
    # 2. 제일 왼쪽 개미가 오른쪽으로 떨어지는 경우 : l - ant[0]
    max_time = max(l-ant[0],ant[-1])
    
    print(min_time,max_time)
    