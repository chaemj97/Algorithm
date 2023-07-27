'''
    접근법
        인접한 4면 중 땅의 개수가 0 or 1이면 사라짐
        사라지지 않은 땅들로 유지될 지도 크기 구하기
    
'''
import sys
input = sys.stdin.readline

r,c = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(r)]

# 50년 뒤 없어질 땅
disappear = []

# 유지될 지도 크기
min_h = 10
max_h = 0
min_l = 10
max_l = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'X':
            cnt = 0
            for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:
                if 0<=i+dr<r and 0<=j+dc<c and arr[i+dr][j+dc] == 'X':
                    cnt += 1
            if cnt <= 1:
                disappear.append((i,j))
            else:
                min_h = min(min_h,i)
                max_h = max(max_h,i)
                min_l = min(min_l,j)
                max_l = max(max_l,j)
                
# 땅 지우기
for i,j in disappear:
    arr[i][j] = '.'

# 결과 출력
for h in range(min_h,max_h+1):
    print(''.join(arr[h][min_l:max_l+1]))