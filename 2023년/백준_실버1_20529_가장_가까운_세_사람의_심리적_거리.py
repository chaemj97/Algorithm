'''
    접근법 
        3명 선택 수 거리 구하기
        -> 완전 탐색
        -> 시간 초과 -> 학생이 33명 이상이면 같은 mbti를 가진 학생이 3명이상 존재

'''
from itertools import combinations
import sys
input = sys.stdin.readline

# 테스트 케이스의 수
T = int(input())
for _ in range(T):
    # 학생의 수
    n = int(input())
    mbti = list(input().split())
    
    # 같은 mbti가 3개 이상인 것이 존재
    if n >= 33:
        print(0)
        continue
    
    # 가장 가까운 세 학생 사이의 심리적 거리
    answer = float('inf')
    # 3명 선택
    for i,j,k in combinations(mbti,3):
        s = 0
        for a in range(4):
            if i[a] != j[a]:
                s += 1
            if i[a] != k[a]:
                s += 1
            if k[a] != j[a]:
                s += 1
        # 가장 가까운가?
        if s < answer:
            answer = s
    print(answer)