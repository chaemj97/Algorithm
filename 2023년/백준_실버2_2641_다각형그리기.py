'''
    접근법 1
        모양수열의 최대개수 100, 각 모양수열의 최대길이 50이니 다 확인하면 100*50=5000
        
        각 좌표를 찍어서 정렬해서 첫번째 위치를 [0,0]으로 바꾸기
        ex) 표준수열 
            [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]
'''

import sys
input = sys.stdin.readline

def make_poly(l):
    d = [[0],[0,1],[-1,0],[0,-1],[1,0]]
    # 각 좌표 찍어보기
    s = [[0,0]]
    for i in l[:-1]:
        r,c = s[-1]
        dr,dc = r+d[i][0], c+d[i][1]
        s.append([dr,dc])
    # 좌표를 정렬해서 첫번째 위치를 [0,0]으로 바꾸기
    s.sort()
    sr,sc = s[0]
    s = [[i-sr,j-sc] for i,j in s]
    return s

# 표본 모양수열의 길이 
n = int(input())
standard = make_poly(list(map(int,input().split())))

answer = []
# 모양수열
m = int(input())
for _ in range(m):
    a = list(map(int,input().split()))
    arr = make_poly(a)
    # 표준과 일치하는가?
    if arr == standard:
        answer.append(a)
        
print(len(answer))
for i in answer:
    print(*i)
        
        