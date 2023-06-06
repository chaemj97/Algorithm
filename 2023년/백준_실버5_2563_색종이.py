'''
    접근법
        모든 색종이의 영역 표시하기
    
'''

import sys
input = sys.stdin.readline

# 색종이의 수
n = int(input())
# 전체 영역
arr = [[0]*101 for _ in range(101)]

answer = 0
# 색종이의 왼쪽 아래 모서리 위치
for _ in range(n):
    a,b = map(int,input().split())
    for r in range(a,a+10):
        for c in range(b,b+10):
            if arr[r][c] == 0:
                answer += 1
                arr[r][c] = 1
                
print(answer)
            

