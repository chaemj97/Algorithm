'''
    접근법 1
        추가 게임 횟수 이진 탐색
        승률 int(Y/X*100)으로 하면 틀림
            실수 연산은 부정확 할 수 있기 때문에 주의

'''
import sys
input = sys.stdin.readline

# 게임 횟수, 이긴 게임 수
X, Y = map(int,input().split())

# 승률
Z = Y*100//X

answer = float('inf')
l,r = 1,X
while l <= r:
    # 추가 게임 횟수
    cnt = (l+r)//2
    # 추가 게임 이긴 후 승률
    new_Z = int((Y+cnt)/(X+cnt)*100)

    # 승률이 변했는가?
    if new_Z > Z:
        answer = min(answer,cnt)
        r = cnt - 1
    else:
        l = cnt + 1

# 만약 Z가 절대 변하지 않는다면
if answer == float('inf'):
    print(-1)
else:
    print(answer)















# # 목표 승률
# Z = (int(Y/X*100) + 1)/100
# # print(Z)
# answer = math.ceil((Z*X-Y)/(1-Z))

# if answer <= 0:
#     print(-1)
# else:
#     print(answer)
