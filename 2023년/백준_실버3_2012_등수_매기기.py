'''
    접근법
        불만도 합의 최소값을 구하기
        예상 등수와 실제 등수 차가 최소가 되어야 함
'''

import sys
input = sys.stdin.readline

# 학생의 수
n = int(input())

# 등수
rank = sorted(i for i in range(1,n+1))
# 예상 등수
predict = sorted(int(input()) for _ in range(n))

answer = 0
for i in range(n):
    # 등수와 예상 등수 차
    answer += abs(rank[i]-predict[i])
    
print(answer)