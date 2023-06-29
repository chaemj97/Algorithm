'''
    접근법
        행렬 곱
        answer[r][c] = A[r][0]*B[0][c] + A[r][1]*B[1][c] + ... + A[r][m]*B[m][c]
    
'''
import sys
input = sys.stdin.readline

# 행렬 A의 크기 n,m
n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]

# 행렬 B의 크기 m,k
m,k = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(m)]

# n X k 행렬
answer = [[0]*k for _ in range(n)]

# 행렬 곱
for r in range(n):
    for c in range(k):
        for i in range(m):
            answer[r][c] += A[r][i]*B[i][c]

# 결과 출력
for r in range(n):
    print(*answer[r])