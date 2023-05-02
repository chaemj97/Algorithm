'''
    접근법 1
        접시 최대 3만개, k 최대 3000
        (연속된 k개의 초밥 + 쿠폰 초밥)의 가짓 수가 최대인지 완전 탐색 

'''

import sys
input = sys.stdin.readline

# 접시 수, 초밥 가짓 수, 연속해서 먹는 접시 수, 쿠폰 번호
n,d,k,c = map(int,input().split())
chobab = [int(input()) for _ in range(n)]*2

answer = 0
for i in range(n):
    # 연속된 k개의 초밥 + 쿠폰 초밥
    e = set(chobab[i:i+k] + [c])
    answer = max(answer,len(e))
    
print(answer)