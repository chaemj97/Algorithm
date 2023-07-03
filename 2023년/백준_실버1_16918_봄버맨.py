'''
    접근법
        1s : 그대로
        2s : 모든 곳에 폭탄 설치
        3s : 0s 설치 폭탄 폭발
        4s : 모든 곳에 폭탄 설치 == 2s
        5s : 2s 설치 폭탄 폭발
        6s : == 2s
        7s : == 3s
        8s : == 2s
        9s : == 5s
        
        # 1s [2s 3s 2s,5s] 반복    
        1s : n == 1
        2s : n%2 == 0
        3s : n%4 == 3
        5s : n!= 1 and n%4 == 1
'''
import sys
input = sys.stdin.readline

# RxC 직사각형 격자판, n초 후 상태 
r,c,n = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(r)]

if n == 1:
    # 그대로 출력
    for i in range(r):
        print(''.join(arr[i]))
    sys.exit()

if n%2 == 0:
    for i in range(r):
        print(''.join(['O' for _ in range(c)]))
    sys.exit()

def bomb_explosion(arr):
    # 폭탄 위치
    bomb = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                bomb.append((i,j))
                
    answer = [['O']*c for _ in range(r)]
    for i,j in bomb:
        answer[i][j] = '.'
        for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
            if 0<=i+dr<r and 0<=j+dc<c:
                answer[i+dr][j+dc] = '.'
    return answer

answer3 = bomb_explosion(arr)
if n%4 == 3:
    for i in range(r):
        print(''.join(answer3[i]))
    sys.exit()

answer1 = bomb_explosion(answer3)
if n%4 == 1:
    for i in range(r):
        print(''.join(answer1[i]))