'''
    접근법
        (직접 친구)와 (친구의 친구) 수 합하기
    
'''

import sys
input = sys.stdin.readline

# 사람 수
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

# 친구 구하기
def friend_set(num):
    f = set()
    for i in range(n):
        if arr[num][i] == 'Y':
            f.add(i)
    return f

cnt = 0
for i in range(n):
    # i와 직접 친구
    friend = friend_set(i)
    # i의 친구의 친구 구하기
    two_friend = set()
    for k in friend:
        two_friend |= friend_set(k)
    friend |= two_friend
    cnt = max(cnt, len(friend))
# 모두 친구가 없는 경우 생각
print(max(cnt-1,0))