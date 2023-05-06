'''
    접근법 1
        오른발을 옮기는 경우와 왼발을 옮기는 경우 중 최소인 것 고르기
        
        dp에 모든 경우 다 담기

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

d = list(map(int,input().split()))

# dp[n][l][r] : n번째에 발의 위치가 (l,r)
dp = [[[-1]*5 for _ in range(5)] for _ in range(len(d))]

# a에 있는 발을 b로 옮기기
def move(a,b):
    # 같은 지점 한 번 더 누르기
    if a == b:
        return 1
    # 중앙에 있던 발이 다른 지점으로 이동
    elif a == 0:
        return 2
    # 인접한 지점으로 이동
    elif abs(a-b)%2:
        return 3
    # 반대편으로 이동
    else:
        return 4
    
# 발이(l,r)인 상황에서 n번째 발판을 밟았을 때 소모되는 힘
def step_n(n,l,r):
    global dp
    # 다 밟았다?
    if n >= len(d)-1:
        return 0
    # 이미 구한 경우는 한 번 더 구할 필요 없다.
    if dp[n][l][r] != -1:
        return dp[n][l][r]
    
    # 왼발을 움직이는 경우
    move_left = step_n(n+1,d[n],r) + move(l,d[n])
    # 오른발을 움직이는 경우
    move_right = step_n(n+1,l,d[n]) + move(r,d[n])
    
    # 둘 중 힘이 덜 드는 경우 선택
    min_move = min(move_left,move_right)
        
    dp[n][l][r] = min_move
    return dp[n][l][r]

print(step_n(0,0,0))