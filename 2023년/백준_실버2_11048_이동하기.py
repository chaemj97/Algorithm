'''
    접근법
        위, 왼쪽, 왼쪽대각선위 3개중 더 큰 값 받기
    
'''
import sys
input = sys.stdin.readline

# 미로 크기
n,m = map(int,input().split())
arr = [[0]*(m+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]

for r in range(1,n+1):
    for c in range(1,m+1):
        arr[r][c] += max(arr[r][c-1],arr[r-1][c-1],arr[r-1][c])

print(arr[n][m])