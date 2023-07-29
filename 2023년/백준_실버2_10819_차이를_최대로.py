'''
    접근법
        나열할 수 있는 모든 순서 구하기
            차이의 합이 최대인가?
'''
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

answer = 0
# 모든 순서 경우 확인
for p in permutations(arr,n):
    s = 0
    # 차이의 합 계산
    for i in range(n-1):
        s += abs(p[i]-p[i+1])
    # 차이의 합이 최대?
    answer = max(answer,s)

# 결과 출력
print(answer)