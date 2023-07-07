'''
    접근법 
        구현
    
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(n)]

answer = []
for r in range(n):
    for c in range(m):
        if arr[r][c] == '.':
            flag = False
            # 가로로 이어지는 단서의 시작점
            if c == 0 or arr[r][c-1] == '#':
                if c < m-2 and arr[r][c+1] == '.' and arr[r][c+2] == '.':
                    flag = True
            # 세로로 이어지는 단서의 시작점
            if r == 0 or arr[r-1][c] == '#':
                if r < n-2 and arr[r+1][c] == '.' and arr[r+2][c] == '.':
                    flag = True
            if flag:
                answer.append((r,c)) 
# 결과 출력
print(len(answer))
for i,j in answer:
    print(i+1,j+1)