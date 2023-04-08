'''
    접근법 1
        의상 종류 a,b,c,d 일 때 각 의상의 개수 1,2,3,4 인 경우
        의사 조합 수
            (1+1)(2+1)(3+1)(4+1)-1
            각 의상을 입지 않는 경우도 생각하기
'''

import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    # 의상 수
    n = int(input())
    answer = 1
    # 각 의상의 종류마다 개수
    clothes = {}
    for _ in range(n):
        # 의상의 이름, 의상의 종류
        a,b = input().split()
        clothes[b] = clothes.get(b,0) + 1
    
    # 의상 조합 수 세기
    for i in clothes.values():
        answer *= (i+1)
    print(answer-1)