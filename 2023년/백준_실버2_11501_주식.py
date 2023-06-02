'''
    접근법
        거꾸로 생각해보기
        현재 주식이 미래의 최댓값보다 크면 사자
    
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 날의 수
    n = int(input())
    arr = list(map(int,input().split()))
    
    # 주식을 사고 팔았을 때 최대 이익
    max_profit = 0
    # 주식 최댓값
    max_value = 0
    for i in range(n-1,-1,-1):
        # 최댓값보다 큰 값 -> 최댓값 갱신
        if arr[i] > max_value:
            max_value = arr[i]
        # 최댓값보다 작은 값 -> 사자
        else:
            max_profit += (max_value - arr[i])
    print(max_profit)