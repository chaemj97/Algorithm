'''
    접근법
        경사로 상승 하강 나눠서 생각
    
'''
import sys
input = sys.stdin.readline

# nXn 크기의 지도, 경사로 l칸 차지
n,l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

answer = 0

# 지나갈 수 있는가?
def check_line(line):
    i = 1
    while i < n:
        # 높이 차가 1칸 초과? -> False
        if abs(line[i] - line[i-1]) > 1:
            return False
        # 상승
        if line[i-1] < line[i]:
            # l칸의 경사 놓을 수 있는지 확인
            for k in range(l):
                # 놓을 수 없다 -> False
                # 하강 경사로가 놓이지 않아야 한다.
                if i-k-1 < 0 or line[i-1] != line[i-k-1] or slope[i-k-1]:
                    return False
                
            i += 1
        # 하강
        elif line[i-1] > line[i]:
            # l칸의 경사 놓을 수 있는지 확인
            for k in range(l):
                if i+k >= n or line[i] != line[i+k]:
                    return False
                # 경사로 놓은거 표시 -> 중복 피하기 위해
                else:
                    slope[i+k] = True
            i += l
        else:
            i += 1
    return True

# 가로 확인
for r in range(n):
    slope = [False]*n
    if check_line(arr[r]):
        answer += 1
            
# 세로 확인
for c in range(n):
    slope = [False]*n
    if check_line([arr[r][c] for r in range(n)]):
        answer += 1

# 결과
print(answer)