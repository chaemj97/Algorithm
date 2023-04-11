'''
    접근법 1
        bfs를 돌면서 각 조건에 맞춰 구현

'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(visited):
    global document

    que = deque([[0,0]])
    visited[0][0] = 1
    while que:
        # 현 위치
        cr,cc = que.popleft()
        # 이동
        for dr,dc in [[-1,0],[0,1],[1,0],[0,-1]]:
            nr = cr+dr
            nc = cc+dc
            # 범위 내 + 벽 X + 방문한 적 X
            if 0 <= nr < h+2 and 0 <= nc < w+2 and arr[nr][nc] != '*' and visited[nr][nc] == 0:
                # 문인가? (대문자)
                if 'A' <= arr[nr][nc] <= 'Z':
                    # 문 열 수 없는가? (== 키가 없다.)
                    if arr[nr][nc].lower() not in key:
                        continue
                # 키인가? (소문자)
                elif 'a' <= arr[nr][nc] <= 'z':
                    # 처음 나온 키?
                    if arr[nr][nc] not in key:
                        key[arr[nr][nc]] = True
                        # 새로운 키 나왔으니 방문 다시 해야할 곳 생겼다
                        # 방문체크 초기화
                        visited = [[0]*(w+2)  for _ in range(h+2)]
                # 문서인가? ($) 
                elif arr[nr][nc] == '$' and (nr,nc) not in document:
                    document.append((nr,nc))
                    visited[nr][nc] = 1
                # 방문 표시
                visited[nr][nc] = 1
                que.append([nr,nc])

TC = int(input())
for _ in range(TC):
    # 높이,너비
    h, w = map(int, input().split())
    arr = ['.'*(w+2)] + ['.'+input()+'.' for _ in range(h)] + ['.'*(w+2)]
    visited = [[0]*(w+2) for _ in range(h+2)]

    # 가지고 있는 키
    key = {}
    for i in input():
        # i == 0이면 키 없음
        if i.isalpha():
            key[i] = True
    
    document = []
    bfs(visited)
    print(len(document))

# 메모리 : 34208, 시간 : 1888
