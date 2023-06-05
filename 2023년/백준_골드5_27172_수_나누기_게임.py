'''
    접근법
        전부 다 확인하면 시간초과 남
        각 카드의 배수를 확인

'''

import sys
input = sys.stdin.readline

# 플레이어 수 
n = int(input())
x = list(map(int,input().split()))
# 카드 번호 1부터 1000000 사이의 수 
card = [False]*(1000001)
for i in x:
    card[i] = True

score = [0]*(1000001)

for i in sorted(x):
    # i의 배수
    for j in range(i*2,1000001,i):
        # i의 배수인 j 카드가 존재
        # j%i == 0 -> i 1점 획득, j 1점 차감
        if card[j]:
            score[i] += 1
            score[j] -= 1
            
for i in x:
    print(score[i],end=' ')