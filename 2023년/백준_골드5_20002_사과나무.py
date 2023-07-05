'''
    접근법
        1. 과수원 누적합 구하기
        2. 누적합을 통해 사과나무 총이익 구하기
    
'''
import sys
input = sys.stdin.readline

# 과수원 크기
n = int(input())
# 누적합 구하기
cum_sum = [[0]*(n+1) for _ in range(n+1)]

for r in range(1,n+1):
    # r행 데이터
    data = [0] + list(map(int,input().split()))
    for c in range(1,n+1):
        cum_sum[r][c] = cum_sum[r][c-1] + cum_sum[r-1][c] - cum_sum[r-1][c-1] + data[c]

# 얻을 수 있는 총이익
answer = -1000

for k in range(1,n+1):
    # k : 가질 사과나무 크기
    # (r,c) : 가질 사과나무 시작점
    for r in range(1,n-k+2):
        for c in range(1,n-k+2):
            # (r,c)~(r+k-1,c+k-1)
            cnt = cum_sum[r+k-1][c+k-1] - cum_sum[r-1][c+k-1] - cum_sum[r+k-1][c-1] + cum_sum[r-1][c-1]
            answer = max(answer,cnt)
            
print(answer)