'''
    접근법
        임무 종류 6가지
        수행 일수 최대 8일
        
        완전 탐색 6**8 = 약 168만
    
'''
import sys
input = sys.stdin.readline

# 수행 일수, 최소 기여도
n,m = map(int,input().split())
# 얻을 수 있는 진척도
arr = [list(map(int,input().split())) for i in range(2)]

answer = 0
def choice(i,s,prev):
    global answer
    if i == n:
        if s >= m:
            answer += 1
        return 

    for nr,nc in [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2]]:
        if nc == prev:
            choice(i+1,s+arr[nr][nc]//2,nc)
        else:
            choice(i+1,s+arr[nr][nc],nc) 

choice(0,0,-1)
print(answer)